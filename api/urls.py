from rest_framework import routers
from contact.views import ContactViewset
from product.views import ProductViewset
from login.views import RegisterViewSet, LoginViewSet, LogoutViewSet
from django.contrib.auth import login as auth_login, authenticate
from checkout.views import CheckoutViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

#This Following URL is for APIs
router = DefaultRouter()
router.register(r'contacts', ContactViewset)              
router.register(r'login', LoginViewSet)
router.register(r'logout', LogoutViewSet)
router.register(r'register', RegisterViewSet)
router.register(r'products', ProductViewset)
router.register(r'checkout', CheckoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
]