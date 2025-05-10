# hospital_app/admin.py

from django.contrib import admin
from .models import Patient, Prescription

class PrescriptionInline(admin.TabularInline):
    model = Prescription
    extra = 0

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'patient_name', 'nhs_number', 'date_of_birth')
    search_fields = ('patient_id', 'patient_name', 'nhs_number')
    inlines = [PrescriptionInline]

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('ref_no', 'patient', 'name_of_tablet', 'dose', 'issue_date', 'exp_date')
    list_filter = ('issue_date', 'exp_date')
    search_fields = ('ref_no', 'patient__patient_name', 'name_of_tablet')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Prescription, PrescriptionAdmin)