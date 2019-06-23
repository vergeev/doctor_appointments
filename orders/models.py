from django.conf import settings
from django.db import models

from doctor_appointments.utils import ChoicesEnum


class OrderStatus(ChoicesEnum):
    CREATED = 'Создана'
    IN_PROGRESS = 'Обрабатывается'
    PROCESSED = 'Обработана'
    PATIENT_REFUSED = 'Пациент отказался'


class Order(models.Model):
    clinic = models.ForeignKey(
        'clinics.Clinic',
        verbose_name='Требуемая клиника',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    specialty = models.ForeignKey(
        'clinics.Specialty',
        verbose_name='Требуемый специалист',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    patient = models.ForeignKey(
        'clinics.Patient',
        verbose_name='Заявитель',
        help_text='Пациент, оставивший заявку',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    status = models.CharField(
        'Статус',
        choices=OrderStatus.choices(),
        default=OrderStatus.CREATED,
        max_length=255,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Ответственный оператор',
        related_name='created_orders',
        on_delete=models.CASCADE,
        editable=False,
    )
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    def __str__(self):
        return f'Запись {self.patient.name} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class ConvenientTimeRange(models.Model):
    starts_at = models.DateTimeField('Начало')
    ends_at = models.DateTimeField('Конец')

    def __str__(self):
        return f'Временной промежуток с {self.starts_at.ctime()} до {self.ends_at.ctime()}'

    class Meta:
        abstract = True


class PatientTimeRange(ConvenientTimeRange):
    order = models.ForeignKey(
        Order, related_name='patient_time_ranges', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Удобное для пациента время'
        verbose_name_plural = 'Удобные для пациента временные промежутки'


class ClinicTimeRange(ConvenientTimeRange):
    order = models.ForeignKey(
        Order, related_name='clinic_time_ranges', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Удобное для клиники время'
        verbose_name_plural = 'Удобные для клиники временные промежутки'
