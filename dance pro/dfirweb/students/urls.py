from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('about/', views.about, name='about'), 
    path('login/', views.admin_login, name='admin_login'),
    path('manage_students/', views.manage_students, name='manage_students'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('contact/', views.contact, name='contact'),  # Add this line
]


