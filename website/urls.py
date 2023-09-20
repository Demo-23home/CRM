from django.urls import path

from .views import *


app_name = 'website'


urlpatterns = [
    path('',home,name='home'),
    # path('',login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
]
