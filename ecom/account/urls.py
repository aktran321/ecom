from django.urls import path
from . import views

from django.contrib.auth import views as auth_views



urlpatterns = [
  # main page
  path("register/", views.register, name="register"),
  path("registration/email-verification/<str:uidb64>/<str:token>/", views.email_verification, name="email-verification"),
  path("registration/email-verification-sent/", views.email_verification_sent, name="email-verification-sent"),
  path("registration/email-verification-success/", views.email_verification_success, name="email-verification-success"),
  path("registration/email-verification-failed/", views.email_verification_failed, name="email-verification-failed"),

  # Login/Logout URLS
  path("my-login/", views.my_login, name="my-login"),
  path("user-logout", views.user_logout, name="user-logout"),

  # Dashboard
  path("dashboard/", views.dashboard, name="dashboard"),
  path("profile-management/", views.profile_management, name="profile-management"),
  path("delete-account/", views.delete_account, name="delete-account"),

  # Password Reset
  path("reset_password", auth_views.PasswordResetView.as_view(template_name="account/password/password-reset.html"), name="reset_password"),
  path("reset_password_sent", auth_views.PasswordResetDoneView.as_view(template_name="account/password/password-reset-sent.html"), name="password_reset_done"),
  path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="account/password/password-reset-form.html"), name="password_reset_confirm"),

  # Password Reset Complete
  path("password_reset_complete", auth_views.PasswordResetCompleteView.as_view(template_name="account/password/password-reset-complete.html"), name="password_reset_complete"),

  path('manage-shipping', views.manage_shipping, name='manage-shipping'),
  path('track-orders', views.track_orders, name='track-orders'),
]