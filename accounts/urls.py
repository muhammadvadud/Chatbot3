from django.urls import path
from .views import SinupPage

urlpatterns = [
    path("register/",SinupPage.as_view(), name="register")
]
