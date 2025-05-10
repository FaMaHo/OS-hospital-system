# hospital_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Prescription
from .forms import PatientForm, PrescriptionForm

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Simple view to test if things are working
    return HttpResponse("<h1>Hospital Management System</h1><p>Welcome to the home page!</p>")

def home(request):
    return render(request, 'hospital_app/index.html')

# Patient views
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital_app/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital_app/patient_form.html', {'form': form})

def update_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'hospital_app/patient_form.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'hospital_app/delete_confirm.html', {'object': patient})

# Prescription views
def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'hospital_app/prescription_list.html', {'prescriptions': prescriptions})

def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'hospital_app/prescription_form.html', {'form': form})

def update_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('prescription_list')
    else:
        form = PrescriptionForm(instance=prescription)
    return render(request, 'hospital_app/prescription_form.html', {'form': form})

def delete_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    if request.method == 'POST':
        prescription.delete()
        return redirect('prescription_list')
    return render(request, 'hospital_app/delete_confirm.html', {'object': prescription})

def patient_prescriptions(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    prescriptions = patient.prescriptions.all()
    return render(request, 'hospital_app/patient_prescriptions.html', 
                 {'patient': patient, 'prescriptions': prescriptions})