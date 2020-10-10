from . import views
from django.urls import path

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:id>/<int:quantity>', views.add_to_cart, name='add_to_cart'),
    path('delete_cart/<int:id>/<int:flag>', views.delete_cart, name='delete_cart'),
    path('get_cart_price_details', views.get_cart_price_details),
    path('change_cart_quantity',views.change_cart_quantity)
    
]