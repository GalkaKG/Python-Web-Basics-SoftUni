from django.urls import path
from .views import *

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('details/<int:pk>/', details, name='details'),
)
