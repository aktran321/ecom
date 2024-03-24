from django.shortcuts import render
from . import models

# Create your views here.
def store(request):
  return render(request, 'store/store.html')

def categories(request):
  all_categories = models.Category.objects.all()
  return {
    'all_categories': all_categories
  }