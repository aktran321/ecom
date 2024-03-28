from decimal import Decimal
from store.models import Product

# to check your cart in terminal:

# python manage.py shell
# from django.contrib.sessions.models import Session
# session_key = Session.objects.get(pk = "<your session key>")
# session_key.get_decoded()

# exit()

class Cart():
  def __init__(self, request):
    self.session = request.session
    cart = self.session.get("session_key")
    if "session_key" not in request.session:
      cart = self.session["session_key"] = {}
    self.cart = cart

    # if product is in the cart, we only update quantity
    # if product is not in the cart, we add the product to the cart with price and qty
  def add(self, product, product_qty):
      print("cart.py has added the product to the cart")
      product_id = str(product.id)
      if product_id in self.cart:
        self.cart[product_id]["qty"] = product_qty
      else:
        self.cart[product_id] = {"price": str(product.price), "qty": product_qty}
      self.session.modified = True

  def __len__(self):
    return sum(item["qty"] for item in self.cart.values())
  
  def __iter__(self):
    all_product_ids = self.cart.keys()
    products = Product.objects.filter(id__in=all_product_ids)
    cart = self.cart.copy()
    for product in products:
      cart[str(product.id)]["product"] = product
    for item in cart.values():
      item["price"] = Decimal(item["price"])
      item["total"] = item["price"] * item["qty"]
      yield item

  def get_total(self):
    return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())
  
  def delete(self, product):
    product_id = str(product)
    if product_id in self.cart:
      del self.cart[product_id]
    self.session.modified = True