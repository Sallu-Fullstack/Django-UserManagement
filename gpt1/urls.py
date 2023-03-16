from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users', views.show_users, name='home'),
    path('logout', views.logout, name='logout'),
    path('create-form/', views.create_form, name='create_form'),
]

