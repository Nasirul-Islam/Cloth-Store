from django.shortcuts import render, redirect
from store.models import ProductsModel
from .models import Cart, CartItem
from django.db.models import Q

# Create your views here.
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def cart(request):
    tax=0
    total=0.0
    totalPrice=0
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        for i in cart_items:
            total += i.product.price * i.quantity
    else:
        session_id = get_create_session(request)
        cart_id = Cart.objects.get(cart_id = session_id)
        if cart_id:
            cart_items = CartItem.objects.filter(cart=cart_id)
            for i in cart_items:
                total += i.product.price * i.quantity
    tax = total*0.02
    totalPrice = total+tax
    context = {'cart_items': cart_items, 'total': total, 'tax': tax, 'totalPrice': totalPrice}
    return render(request, 'cart.html', context)

def add_to_cart(request, product_id):
    product = ProductsModel.objects.get(id=product_id)
    session_id = get_create_session(request)
    
    if request.user.is_authenticated: #loged in
        cart_item = CartItem.objects.filter(product=product, user=request.user).exists()
        if cart_item: # item asa
            item = CartItem.objects.get(product=product)
            item.quantity += 1
            item.save()
        else: # item ni 
            cart = Cart.objects.create(cart_id=session_id)
            cart.save()
            item = CartItem.objects.create(
                product = product,
                cart = cart,
                quantity = 1,
                user = request.user,
            )
            item.save()
    else:
        cart_id = Cart.objects.filter(cart_id = session_id).exists()
        if cart_id: # session asa
            cart_item = CartItem.objects.filter(product=product).exists()
            if cart_item: # item asa
                item = CartItem.objects.get(product=product)
                item.quantity += 1
                item.save()
            else: # item ni 
                cart = Cart.objects.get(cart_id = session_id)
                item = CartItem.objects.create(
                    product = product,
                    cart = cart,
                    quantity = 1,
                )
                item.save()  
        else: # session ni
            cart = Cart.objects.create(cart_id=session_id)
            cart.save()
            item = CartItem.objects.create(
                    product = product,
                    cart = cart,
                    quantity = 1,
                )
            item.save()
    return redirect('cart')

def minus_item(request, product_id):
    product = ProductsModel.objects.get(id=product_id)
    session_id = request.session.session_key
    cart_id = Cart.objects.get(cart_id = session_id)
    cart_item = CartItem.objects.get(cart=cart_id, product = product)
    if cart_item.quantity>1: 
        cart_item.quantity -= 1
        cart_item.save()
    else: 
        cart_item.delete()
    return redirect('cart')

def remove_item(request, product_id):
    product = ProductsModel.objects.get(id=product_id)
    session_id = request.session.session_key
    cart_id = Cart.objects.get(cart_id = session_id)
    cart_item = CartItem.objects.get(cart=cart_id, product = product) 
    cart_item.delete()
    return redirect('cart')
