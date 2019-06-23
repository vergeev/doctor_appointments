# Generated by Django 2.2.2 on 2019-06-23 12:01

from django.db import migrations


OPERATOR_PERMISSION_CODENAMES = [
    'add_patient', 'change_patient', 'delete_patient', 'view_patient',
    'add_clinictimerange', 'change_clinictimerange', 'delete_clinictimerange',
    'view_clinictimerange',
    'add_order', 'change_order', 'delete_order', 'view_order',
    'add_patienttimerange', 'change_patienttimerange', 'delete_patienttimerange',
    'view_patienttimerange'
]


def add_operator_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    operator_group, _ = Group.objects.get_or_create(name='Оператор')
    permissions = Permission.objects.filter(
        codename__in=OPERATOR_PERMISSION_CODENAMES).all()

    # the permissions were automatically created because the models were too
    operator_group.permissions.add(*permissions)


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_appointment_time'),
    ]

    operations = [
        migrations.RunPython(add_operator_group)
    ]