from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from checkout.forms import CheckoutForm
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail, BadHeaderError
from cart.views import get_total_quantity_in_cart
from cart.models import Cart
from cart.views import get_cart_price_details

# Create your views here.
def checkout(request):
   carts = Cart.objects.all()
   price_details = get_cart_price_details(carts)
   if len(carts) < 1:
      return redirect('/cart')
   quantity=get_total_quantity_in_cart() 
   csrfContext = RequestContext(request)
   checkout_form = CheckoutForm()
   return render(request,'checkout.html',
      {
         "quantity":quantity,
         'form': checkout_form,
         "active_tab":"checkout",
         "request":request,
         "carts": carts,
         "price_details": price_details
      },
      csrfContext) 

class CheckoutViewSet(viewsets.ModelViewSet):
   queryset = models.Checkout.objects.all()
   serializer_class = serializers.CheckoutSerializer
   def create(self, request):
     print("new request")
     serializer = self.get_serializer(data=request.data)
     if serializer.is_valid():
        serializer.save()

        country= request.data.get("country")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        company_name = request.data.get("company_name")
        first_address = request.data.get("first_address")
        second_address = request.data.get("second_address")
        town = request.data.get("town")
        state = request.data.get("state")
        zip_code = request.data.get("zip_code")
        email_address = request.data.get("email_address")
        phone_number = request.data.get("phone_number")
        payment_option = request.data.get("payment_option")
        terms_agreed = request.data.get("terms_agreed")
        message = "Country: " + country + "\nFirst Name: " + first_name + "\nLast Name: " + last_name + "\nCompany Name: " + company_name + "\nFirst Address: " + first_address + "\nSecond Addrress: " + second_address + "\nTown: " + town + "\nState: " + state + "\nZip Code: " + str(zip_code) + "\nEmail Address: " + email_address + "\nPhone Number: " + phone_number + "\nPayment Option: " + payment_option + "\nTerms Agreed: " + terms_agreed
        
        try:
           send_mail("New Order", message, "", [email_address])
        except BadHeaderError:
           return Response(status=500,data={'msg':'Invalid header found.'})
        return Response(status=200,data={"msg": "Your order has been submitted."})
     else:
        return Response(status=500,data={"msg": "Order is invalid."})

 
   def retrieve(self, request, pk=None):
      return Response(status=403,data={"msg": "API not allowed."})

   def update(self, request, pk=None):
       return Response(status=403,data={"msg": "API not allowed."})

   def partial_update(self, request, pk=None):
       return Response(status=403,data={"msg": "API not allowed."})

   def destroy(self, request, pk=None):
       return Response(status=403,data={"msg": "API not allowed."})