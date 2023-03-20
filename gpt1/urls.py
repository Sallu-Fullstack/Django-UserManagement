from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_users, name='users'),
    path('users', views.show_users, name='users'),
    path('index', views.login, name='index'),
    path('logout', views.logout, name='logout'),
    path('show_users', views.show_users, name='show_users'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('create-form/', views.create_form, name='create-form'),
    path('search_username/', views.search_username, name='search_username'),
]
