# hospital_app/models.py

from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=100, primary_key=True)
    nhs_number = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    patient_address = models.TextField()
    
    def __str__(self):
        return f"{self.patient_name} ({self.patient_id})"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    name_of_tablet = models.CharField(max_length=100)
    ref_no = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    number_of_tablets = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    issue_date = models.DateField()
    exp_date = models.DateField()
    daily_dose = models.CharField(max_length=100)
    side_effect = models.CharField(max_length=200, blank=True, null=True)
    further_info = models.TextField(blank=True, null=True)
    storage_advice = models.CharField(max_length=100)
    driving_using_machine = models.CharField(max_length=100, blank=True, null=True)
    how_to_use_medication = models.CharField(max_length=100, blank=True, null=True)
    blood_pressure = models.CharField(max_length=100, blank=True, null=True)
    medication = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.patient.patient_name} - {self.ref_no}"