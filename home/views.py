from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from product.models import Product
from cart.views import get_total_quantity_in_cart

# Create your views here.
def home(request): 
   quantity=get_total_quantity_in_cart() 
   products = Product.objects.all() 
   print("products", products)
   template = loader.get_template('index.html')
   return HttpResponse(template.render({"quantity":quantity,"active_tab":"home","request":request,'products':products}))