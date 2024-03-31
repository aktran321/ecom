from django.urls import path
from . import views

urlpatterns = [
  # main page
  path("register/", views.register, name="register"),
  path("registration/email-verification/<str:uidb64>/<str:token>/", views.email_verification, name="email-verification"),
  path("registration/email-verification-sent/", views.email_verification_sent, name="email-verification-sent"),
  path("registration/email-verification-success/", views.email_verification_success, name="email-verification-success"),
  path("registration/email-verification-failed/", views.email_verification_failed, name="email-verification-failed"),

  # Login/Logout URLS
  path("my-login/", views.my_login, name="my-login"),
  path("dashboard/", views.dashboard, name="dashboard"),
]