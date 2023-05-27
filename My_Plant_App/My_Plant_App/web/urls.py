from django.urls import path, include


from . import views

urlpatterns = (
    path('', views.index, name='home'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.plant_create, name='plant create'),
    path('details/<int:pk>/', views.plant_details, name='plant details'),
    path('edit/<int:pk>/', views.plant_edit, name='plant edit'),
    path('delete/<int:pk>/', views.plant_delete, name='plant delete'),
    path('profile/', include([
        path('create/', views.profile_create, name='profile create'),
        path('details/', views.profile_details, name='profile details'),
        path('edit/', views.profile_edit, name='profile edit'),
        path('delete/', views.profile_delete, name='profile delete'),
    ])),
)


# TODO:
'''
    •	http://localhost:8000/ - home page  - DONE!
    •	http://localhost:8000/catalogue/ - catalogue  - DONE!
    
      •	http://localhost:8000/profile/create/ - profile create page  - DONE!
    •	http://localhost:8000/profile/details/ - profile details page - DONE!
    •	http://localhost:8000/profile/edit/ - profile edit page
    •	http://localhost:8000/profile/delete/ - profile delete page
    
    •	http://localhost:8000/create/ - plant create page  - DONE!
    •	http://localhost:8000/details/<plant_id>/ - plant details page - DONE!
    •	http://localhost:8000/edit/<plant_id>/ - plant edit page  - DONE!
    •	http://localhost:8000/delete/<plant_id>/ - plant delete page  - DONE!
    
   

'''