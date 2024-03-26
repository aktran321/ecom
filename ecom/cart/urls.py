from django.urls import path
from . import views

urlpatterns = [
  # main page
  path ('', views.cart_summary, name='cart-summary'),
  path('add/<int:product_id>/', views.cart_add, name='cart-add'),
  path('delete/<int:product_id>/', views.cart_delete, name='cart-delete'),
  path('update/<int:product_id>/', views.cart_update, name='cart-update'),
]