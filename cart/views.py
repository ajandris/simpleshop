import uuid

from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from products.models import Product, Images


# Create your views here.

def view_cart(request):
    template = 'cart/cart.html'
    cart_no = request.session['cart_number']
    carts = Cart.objects.filter(cart_number=cart_no)
    ctxt = dict()
    if carts is not None:
        cart_items = CartItem.objects.filter(cart=carts[0])
        ctxt = {
            'cart': carts[0],
            'cart_items': cart_items,
        }

    return render(request, template, context=ctxt)

def remove_from_cart(request):
    cart_no = request.session.get('cart_number')
    if request.method != 'POST' or cart_no is None:
        return view_cart(request)

    carts = Cart.objects.filter(cart_number=cart_no)
    if carts is not None:
        sku = request.POST['sku']
        cart = carts[0]
        cart_items = CartItem.objects.filter(cart=cart, product__sku=sku)
        cart_items.delete()
        cart_items = CartItem.objects.filter(cart=cart)
        if cart_items is None:
            cart.delete()
            request.session.pop('cart_number', None)
            request.session.modified = True

    return view_cart(request)


def add_product(request):
    """
    Adds product to cart
    """
    if request.method == 'POST':
        sku = request.POST['sku']
        quantity = int(request.POST.get('quantity')) if request.POST.get('quantity') is not None else 1
        print(sku, quantity)
        cart_no = request.session.get('cart_number')
        if cart_no is None:
            uuid_str = str(uuid.uuid4())
            cart_no = uuid_str.replace("-", "")

        carts = Cart.objects.get_or_create(cart_number=cart_no)
        cart = carts[0]
        if request.user.is_authenticated:
            cart.owner = request.user
            cart.user = request.user
        cart.save()

        product = Product.objects.get(sku=sku)
        cart_items = CartItem.objects.filter(id=cart.id, product=product)

        quantity = int(request.POST.get('quantity')) if request.POST.get('quantity') is not None else 1

        if not cart_items:
            cart_item = CartItem.objects.create(cart=cart, product=product, qty=quantity, price=product.price)
            cart_item.save()
        else:
            cart_item = cart_items[0]
            cart_item.qty = cart_item.qty + quantity
            cart_item.save()

        request.session['cart_number'] = cart_no
        request.session.modified = True  # optional, ensures session is saved

    return redirect(request.META.get('HTTP_REFERER', '/cart/'))


def pay_now(request, sku):
    """
    Pays for chosen product

    1. create a cart
    2. redirect cart to payment page
    """
    pass