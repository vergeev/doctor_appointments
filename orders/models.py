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

    def __str__(self):
        return f'Запись {self.patient.name} ({self.get_status_display()})'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
