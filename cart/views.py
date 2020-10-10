from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product
from cart.models import Cart
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def get_total_quantity_in_cart(carts = None):
    quantity = 0
    if carts is None:
        carts = Cart.objects.all()
    for cart in carts:
        quantity = quantity + cart.quantity
    return quantity

def get_cart_price_details(request):
    carts = Cart.objects.all()
    sub_total = 0
    for cart in carts:
        sub_total = sub_total + cart.total
    delivery_charge = 0
    discount = 0
    total = 0
    if sub_total > 0:
        delivery_charge = 50
        discount = (5/100) * sub_total
        total = delivery_charge + (sub_total - discount)
    
    details = {
        "sub_total": sub_total,
        "delivery_charge": delivery_charge,
        "discount": discount,
        "total": total
    }
    return JsonResponse(details)

def cart (request):
    carts = Cart.objects.all()
    quantity=get_total_quantity_in_cart(carts)
    template = loader.get_template('cart.html')
    return HttpResponse(template.render({"quantity": quantity,"carts":carts, "active_tab":"cart","request":request}))


def add_to_cart(request,id, quantity):
    cart = Cart.objects.all()
    product = Product.objects.get(id=id)
    matching_products = list(filter(lambda d: d.product.id == id, cart))
    if len(matching_products) > 0:
        product_cart = matching_products[0]
        if product_cart is not None:
            product_quantity = product_cart.quantity + quantity
            total = product_quantity * product.pprice
            product_cart.total = total
            product_cart.quantity = product_quantity
            product_cart.save()

    else:
        total = quantity * product.pprice
        cart = Cart(product = product, quantity = int(quantity), total = total)
        cart.save()

    
    return redirect('/cart/')

def delete_cart(request, id, flag):
    cart = Cart.objects.get(id=id)
    cart.delete()
    if flag == 0:
        return redirect('/checkout/')
    else:
        return redirect('/cart/')

@csrf_exempt
def change_cart_quantity(request):
   try:
       carts = Cart.objects.all()
       cart_id = int(request.POST.get("cart_id"))
       new_quantity = int(request.POST.get("new_quantity"))
       cart_list = list(filter(lambda cart: cart.id == cart_id, carts))
       cart = cart_list[0]
       if cart is not None:
           cart.quantity = new_quantity
           cart.total = new_quantity * cart.product.pprice
           cart.save()
           return JsonResponse({'success': True})
       else: 
           return JsonResponse({'success': False})
   except:
       return JsonResponse({'success': False})












