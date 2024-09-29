from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('doctor/dashboard',views.dashboard,name='dashboard'),
    path('doctor/login',views.doctor_login,name='doctor_login'),
    path('doctor/registration',views.doctor_registration,name='doctor_registration'),
    path('doctor/reset-password',views.doctor_reset_password,name='doctor_reset_password'),
    path('doctor/logout',views.doctor_logout,name='doctor_logout'),
    path('doctor/add_patient',views.add_patient,name='add_patient'),
]