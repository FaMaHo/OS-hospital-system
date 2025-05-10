# hospital_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<str:pk>/update/', views.update_patient, name='update_patient'),
    path('patients/<str:pk>/delete/', views.delete_patient, name='delete_patient'),
    
    # Prescription URLs
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/add/', views.add_prescription, name='add_prescription'),
    path('prescriptions/<int:pk>/update/', views.update_prescription, name='update_prescription'),
    path('prescriptions/<int:pk>/delete/', views.delete_prescription, name='delete_prescription'),
    
    # Combined views
    path('patients/<str:patient_id>/prescriptions/', views.patient_prescriptions, name='patient_prescriptions'),
]