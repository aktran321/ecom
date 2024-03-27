from .cart import Cart

# This function will add the cart to the context of every request
# so its available on every template

# it is placed in the settings.py as well
def cart(request):
  return {"cart": Cart(request)}