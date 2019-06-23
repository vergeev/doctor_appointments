from django.db import models


class ContactPhoneField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Контактный телефон'
        kwargs['max_length'] = 16
        kwargs['help_text'] = 'В формате +7(999)123-45-67'
        super().__init__(*args, **kwargs)
