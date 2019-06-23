from django.contrib import admin

from orders.models import Order, PatientTimeRange, ClinicTimeRange


class PatientTimeRangeInline(admin.TabularInline):
    model = PatientTimeRange
    extra = 1


class ClinicTimeRangeInline(admin.TabularInline):
    model = ClinicTimeRange
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ['patient']
    inlines = [PatientTimeRangeInline, ClinicTimeRangeInline]
    save_on_top = True
    readonly_fields = ['created_by', 'created_at', 'updated_at']
    list_filter = ['patient', 'clinic', 'created_by', 'status']
    date_hierarchy = 'created_at'
    search_fields = ['patient__name', 'specialty__title', 'clinic__name']
    list_display = [
        'patient',
        'specialty',
        'clinic',
        'status',
        'appointment_time',
        'created_at',
    ]

    fieldsets = (
        ('Дежурная информация', {
            'classes': ('collapse', 'wide'),
            'fields': (
                'created_by',
                'created_at',
                'updated_at',
            ),
        }),
        (None, {
            'fields': (
                'clinic',
                'specialty',
                'patient',
                'status',
                'appointment_time',
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, 'created_by'):
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
