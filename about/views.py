from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from cart.views import get_total_quantity_in_cart
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/login')
def about(request): 
   quantity=get_total_quantity_in_cart() 
   template = loader.get_template('about.html')
   return HttpResponse(template.render({"quantity":quantity,"active_tab":"about","request":request}))     