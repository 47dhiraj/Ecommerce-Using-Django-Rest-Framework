from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from . import models
from . import serializers
from django.core.mail import send_mail, BadHeaderError
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from contact.forms import ContactForm
from django.template import RequestContext
import requests                      

@csrf_protect
def contact(request): 

   if request.method == 'POST':              
      form = ContactForm(request.POST)   
      if form.is_valid():
         response = requests.post('http://localhost:8000/api/v1/contacts/', request.POST)                    
         print('response', response.text)
         if response.status_code == 200:
            csrfContext = RequestContext(request)
            return render(request,'success.html',
               {
                  "active_tab":"contact",
                  "request":request
               },
               csrfContext) 
         else:
            return HttpResponse("Your query could not be submitted. Please try again.")

   contact_form = ContactForm()         
   csrfContext = RequestContext(request)
   return render(
      request,'contact.html',           
      {
         'form': contact_form,
         "active_tab":"contact",
         "request":request
      },
      csrfContext
   )
   


class ContactViewset(viewsets.ModelViewSet):                 
   queryset = models.Contact.objects.all()
   serializer_class = serializers.ContactSerializer


   def create(self, request):                
     print("new request")
     serializer = self.get_serializer(data=request.data)
     if serializer.is_valid():
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        message = request.data.get("message")
        subject = request.data.get("subject")
        serializer.save()
        try:
           send_mail(subject + ": " + first_name + " " + last_name, 
              message + "\n" + "User email: " + email, "", [email]) 
        except BadHeaderError:
           return Response(status=500,data={'msg':'Invalid header found.'})
        return Response(status=200,data={"msg": "Your query has been submitted."})
     else:
        return Response(status=500,data={"msg": "Query is invalid."})

   def list(self, request):
      return Response(status=403,data={"msg": "API not allowed."})
 
   def retrieve(self, request, pk=None):
      return Response(status=403,data={"msg": "API not allowed."})

   def update(self, request, pk=None):
       return Response(status=403,data={"msg": "API not allowed."})

   def partial_update(self, request, pk=None):
       return Response(status=403,data={"msg": "API not allowed."})

   def destroy(self, request, pk=None):
       return Response(status=403,data={"msg": "API not allowed."})