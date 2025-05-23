from .models import Cart
import uuid

def cart_renderer(request):
      print(type(request))
      try:
         cart = Cart.objects.get(session_id = request.session['nonuser'], completed=False)
      except:
         request.session['nonuser'] = str(uuid.uuid4())
         cart = Cart.objects.create(session_id = request.session['nonuser'], completed=False)
         print("done")
      return {
         'cart': cart
      }