from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('services/', views.services, name = 'services'),
    path('technologies/', views.technologies, name = 'technologies'),
    path('contacts/', views.contacts, name = 'contacts'),
]
