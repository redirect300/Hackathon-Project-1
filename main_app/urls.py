
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('emergency/', views.EmergencyPage, name="emergencyPage"),
    path('consultancy/', views.consultancyPage, name="consultancyPage"),
    path('hospitals/', views.hospitalsPage, name="hospitalsPage"),
    path('registration/', views.registrationPage, name="registrationPage"),
    path('hospitals/dashboard/<str:name>', views.dashboard, name="dashboard"),
    path('logout/',views.logoutPage, name="logout"),
]
