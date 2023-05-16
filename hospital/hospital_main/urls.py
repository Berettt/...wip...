from django.urls import path
from .views import *
app_name = 'hospital_main'

urlpatterns = [
    path('home',Home.as_view(),name='home'),
    path('login/',LoginView,name='login'),
    path('register/',RegisterView,name='register'),
    path('logout/',Logout.as_view(),name="logout")
               
]