from django.contrib import admin

from clinics.models import Clinic, Specialty, Patient


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'passport_number', 'contact_number']
    search_fields = ['name', 'passport_number', 'contact_number']


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    search_fields = ['name', 'address', 'contact_number']
    raw_id_fields = ['specialties']
