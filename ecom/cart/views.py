from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def cart_summary(request):
  cart = Cart(request)

  return render(request, "cart/cart-summary.html", {"cart": cart})

@require_POST
def cart_add(request):
    print("cart_add")
    cart = Cart(request)
    response = JsonResponse({"error": "The action is not specified or incorrect."}, status=400)  # Default response

    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        product_quantity = int(request.POST.get("product_quantity"))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__()
        
        response = JsonResponse({"qty": cart_quantity})
  
    return response

def cart_delete(request):

  cart = Cart(request)
  if request.POST.get("action") == "post":
    product_id = int(request.POST.get("product_id"))
    print("product_id: ", product_id)
    cart.delete(product=product_id)
    
    # after deletion, we update the cart quantity
    cart_quantity = cart.__len__()

    cart_total = cart.get_total()

    response = JsonResponse({"qty": cart_quantity, "total": cart_total})

  return response

def cart_update(request):
  cart = Cart(request)
  if request.POST.get("action") == "post":
    product_id = int(request.POST.get("product_id"))
    print("product_id: ", product_id)
    product_quantity = int(request.POST.get("product_quantity"))

    cart.update(product=product_id, qty=product_quantity)

    cart_quantity = cart.__len__()
    cart_total = cart.get_total()
    response = JsonResponse({"qty": cart_quantity, "total": cart_total})
  return response