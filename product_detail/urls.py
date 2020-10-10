from . import views
from django.urls import path

urlpatterns = [
    
    path('<int:id>', views.new_product_detail),

    
]