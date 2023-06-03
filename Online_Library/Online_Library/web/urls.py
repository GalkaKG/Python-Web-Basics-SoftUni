from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.index, name='home page'),
    path('add/', views.add_book, name='add book'),
    path('edit/<int:pk>/', views.edit_book, name='edit book'),
    path('details/<int:pk>/', views.book_details, name='details book'),
    path('delete/<int:pk>/', views.delete_book, name='delete book'),
    path('profile/', include([
        path('', views.profile_page, name='profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ]))
)
