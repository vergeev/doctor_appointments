from django.db import models


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
    contact_number = models.CharField(
        'Контактный телефон',
        max_length=16,
        help_text='В формате +7(999)123-45-67',
    )
    specialties = models.ManyToManyField(
        Specialty,
        verbose_name='Доступные специальности',
        related_name='clinics'
    )

    def __str__(self):
        return f'{self.name} ({self.contact_number})'

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'
