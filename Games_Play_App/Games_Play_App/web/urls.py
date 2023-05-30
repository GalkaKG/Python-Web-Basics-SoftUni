from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.index, name='home page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', views.create_profile, name='create profile'),
        path('details/', views.details_profile, name='details profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ])),
    path('game/', include([
        path('create/', views.create_game, name='create game'),
        path('details/<int:pk>/', views.details_game, name='details game'),
        path('edit/<int:pk>/', views.edit_game, name='edit game'),
        path('delete/<int:pk>/', views.delete_game, name='delete game'),
    ])),
)
