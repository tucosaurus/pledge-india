from django.urls import path
from .views import *
# urlpatterns

app_name = "pledge"

urlpatterns = [
    path("", HomeView, name="home"),
]
