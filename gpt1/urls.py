from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-form/', views.create_form, name='create_form'),
]
