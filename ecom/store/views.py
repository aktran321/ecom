from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404
import boto3
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_ratelimit.decorators import ratelimit

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

def product_info(request, product_slug):
  product = get_object_or_404(models.Product, slug=product_slug)
  context = {
    'product': product
  }
  return render(request, 'store/product-info.html', context)

def list_category(request, category_slug = None):
  category = get_object_or_404(models.Category, slug=category_slug)
  products = models.Product.objects.filter(category=category)
  context = {
    'category': category,
    'products': products
  }
  return render(request, 'store/list-category.html', context)

# Kinesis Data Streams, to monitor data on who checks out the website
@csrf_exempt
@ratelimit(key="ip", rate="5/m", block=True, method="POST")
def send_page_view(request):
  if request.method == "POST":
    try:
      data = json.loads(request.body) # Parse JSON string and convert to Python object
      # tries to get the userID or fallback on the session ID, to create a partition key
      # this is to spread out data across shards in Kinesis Data Streams
      print(request.body)
      print("Data: ")
      print(data)
      partition_key = data.get("user_id") or data.get("session_id")

      kinesis_client = boto3.client("kinesis", region_name = "us-east-1")
      kinesis_client.put_record(
        StreamName="shoptop-KdsDataStream4BCE778D-QWs4b3y3tqfE",
        Data=json.dumps(data), #serialize python object into a JSON formatted string
        PartitionKey=str(partition_key)
      )

      return JsonResponse({"status": "success", "message": "Data sent to Kinesis."}, status=200)
    except Exception as e:
      return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
  # if request is not a POST, send error
  else:
    return JsonResponse({"status": "error", "message": "Invalid request"})

