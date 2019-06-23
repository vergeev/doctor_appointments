from django.db import models

from clinics.model_fields import ContactPhoneField


class Specialty(models.Model):
    title = models.CharField('Название', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Clinic(models.Model):
    name = models.CharField('Название', max_length=32)
    address = models.CharField('Адрес', max_length=128)
    contact_number = ContactPhoneField()
    specialties = models.ManyToManyField(
        Specialty,
        verbose_name='Доступные специальности',
        related_name='clinics',
    )

    def __str__(self):
        return f'{self.name} ({self.contact_number})'

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'


class Patient(models.Model):
    name = models.CharField('ФИО', max_length=256)
    passport_number = models.CharField(
        'Серия и номер паспорта',
        max_length=10,
        help_text='10 цифр без пробелов',
    )
    contact_number = ContactPhoneField()

    def __str__(self):
        return f'{self.name} ({self.contact_number})'

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
