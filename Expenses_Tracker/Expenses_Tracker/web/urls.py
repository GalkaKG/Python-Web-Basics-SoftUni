from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.home, name='home page'),
    path('create/', views.create, name='create expense'),
    path('edit/<int:pk>/', views.edit, name='edit expense'),
    path('delete/<int:pk>/', views.delete, name='delete expense'),
    path('profile/', include([
        path('', views.profile_page, name='profile page'),
        path('edit/', views.profile_edit, name='edit profile'),
        path('delete/', views.profile_delete, name='delete profile'),
    ])),
)
