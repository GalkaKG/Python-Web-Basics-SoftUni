from django.urls import path
from . import views

urlpatterns = (
    path('', views.home, name='home page'),
    path('profile/', views.profile_page, name='profile'),
    path('delete/', views.profile_delete, name='delete profile'),
    path('add/', views.add_note, name='add note'),
    path('edit/<int:pk>/', views.edit_note, name='edit note'),
    path('delete/<int:pk>/', views.delete_note, name='delete note'),
    path('details/<int:pk>/', views.details_note, name='details note'),
)
