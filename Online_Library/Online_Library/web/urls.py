from django.urls import path, include
from . import views

urlpatterns = (
    path('', views.index, name='home page'),
    path('add/', views.add_book, name='add book'),
    path('edit/<int:pk>/', views.edit_book, name='edit book'),
    path('details/<int:pk>/', views.book_details, name='details book'),
    path('profile/', include([
        path('', views.profile, name='profile'),
        path('edit/', views.edit_profile, name='edit profile'),
        path('delete/', views.delete_profile, name='delete profile'),
    ]))
)


# TODO:

'''
•	http://localhost:8000/ - home page

•	http://localhost:8000/add/ - add book page
•	http://localhost:8000/edit/:id - edit book page
•	http://localhost:8000/details/:id - book details page

•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - edit profile page
•	http://localhost:8000/profile/delete/ - delete profile page0
'''