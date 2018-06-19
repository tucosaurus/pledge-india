from django.urls import path
from .views import JsonData
# urlpatterns

urlpatterns = [
    path("get/", JsonData, name="get-pledges"),
]
