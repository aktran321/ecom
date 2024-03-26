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
      product_id = str(product.id)
      if product_id in self.cart:
        self.cart[product_id]["qty"] = product_qty
      else:
        self.cart[product_id] = {"price": str(product.price), "qty": product_qty}
      self.session.modified = True