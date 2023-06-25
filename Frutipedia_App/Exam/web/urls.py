from django.urls import path, include
from . import views


urlpatterns = (
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_fruit, name='create fruit'),
    path('<int:pk>/', include([
        path('details/', views.details_fruit, name='details fruit'),
        path('edit/', views.edit_fruit, name='edit fruit'),
        path('delete/', views.delete_fruit, name='delete fruit'),
    ])),
    path('profile/', include([
        path('create/', views.create_profile, name='create profile'),
        path('details/', views.details_profile, name='details profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ])),
)



