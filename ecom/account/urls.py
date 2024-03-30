from django.urls import path
from . import views

urlpatterns = [
  # main page
  path("register/", views.register, name="register"),
]