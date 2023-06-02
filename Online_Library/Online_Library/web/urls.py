from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='home page'),
    path('add/', views.add_book, name='add book'),

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