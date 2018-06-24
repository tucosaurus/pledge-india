from django.urls import path, include

from django.contrib.auth import views
from .views import *

app_name="user"

urlpatterns = [
    path("", HomeView, name="user-home"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
