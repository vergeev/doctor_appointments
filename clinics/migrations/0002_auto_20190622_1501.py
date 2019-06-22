# Generated by Django 2.2.2 on 2019-06-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterField(
            model_name='clinic',
            name='contact_number',
            field=models.CharField(help_text='В формате +7(999)123-45-67', max_length=16, verbose_name='Контактный телефон'),
        ),
    ]