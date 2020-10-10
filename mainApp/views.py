from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse

def layout(request):  
   template = loader.get_template('layout.html')
   return HttpResponse(template.render())