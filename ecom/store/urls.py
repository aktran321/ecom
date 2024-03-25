from django.urls import path
from . import views

urlpatterns = [
  # main page
  path ('', views.store, name='store'),
  # individual item
  path ('product/<slug:product_slug>/', views.product_info, name='product-info'),
  # individual category
  path ('category/<slug:category_slug>/', views.list_category, name='list-category'),
]