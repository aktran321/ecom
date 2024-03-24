from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.
def store(request):
  all_products = models.Product.objects.all()
  context = {
    'my_products': all_products
  }
  return render(request, 'store/store.html', context)


def categories(request):
  all_categories = models.Category.objects.all()
  return {
    'all_categories': all_categories
  }

def product_info(request, slug):
  product = get_object_or_404(models.Product, slug=slug)
  context = {
    'product': product
  }
  return render(request, 'store/product-info.html', context)
