import uuid

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from cart.models import Cart, CartItem, Coupon, Shipping
from products.models import Product
from django.contrib import messages



# Create your views here.

def view_cart(request):
    template = 'cart/cart.html'
    cart_no = request.session['cart_number']
    carts = Cart.objects.filter(cart_number=cart_no)
    ctxt = dict()
    shipping = Shipping.objects.all().order_by('price')
    if carts is not None:
        cart_items = CartItem.objects.filter(cart=carts[0])
        coupon = None
        if carts[0].discount is not None:
            coupon = Coupon.objects.filter(id=carts[0].discount.id).first()
        ctxt = {
            'cart': carts[0],
            'cart_items': cart_items,
            'coupon': coupon,
            'shipping': shipping
        }

    return render(request, template, context=ctxt)

def remove_from_cart(request):
    """
    Remove a product from the cart
    """
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

    messages.success(request, "Item removed from cart successfully!")

    return redirect('cart')


def add_product(request):
    """
    Adds product to cart
    """
    if request.method == 'POST':
        sku = request.POST['sku']
        quantity = int(request.POST.get('quantity')) if request.POST.get('quantity') is not None else 1
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
        cart_items = CartItem.objects.filter(cart=cart, product=product)

        quantity = int(request.POST.get('quantity')) if request.POST.get('quantity') is not None else 1

        if cart_items.count() == 0:
            cart_item = CartItem.objects.create(cart=cart, product=product, qty=quantity, price=product.price)
            cart_item.save()
        else:
            cart_item = cart_items[0]
            if cart_item.product == product:
                cart_item.qty = cart_item.qty + quantity
            else:
                cart_item.qty = quantity
            cart_item.save()

        request.session['cart_number'] = cart_no
        request.session.modified = True  # optional, ensures session is saved

        messages.success(request, "Item added to cart successfully!")

    return redirect(request.META.get('HTTP_REFERER', 'cart'))


def add_coupon(request):
    """
    Adds a coupon to cart
    """
    success = False
    if request.method == "POST":
        if request.POST.get('coupon'):
            coupon = request.POST.get('coupon').strip().upper()
            coup = Coupon.objects.filter(code__iexact=coupon).first()
            if request.session.get('cart_number'):
                cart_no = request.session.get('cart_number')
                cart = Cart.objects.filter(cart_number=cart_no).first()
                if cart is not None and coup is not None:
                    cart.discount = coup
                    cart.save()
                    success = True

    if success:
        messages.success(request, "Coupon added to cart")
    else:
        messages.error(request, "Coupon is not added to cart")

    return redirect('cart')


def remove_coupon(request):
    """
    Removes a coupon from cart
    """
    success = False
    if request.method == "POST":
        if request.POST.get('coupon'):
            if request.session.get('cart_number'):
                cart_no = request.session.get('cart_number')
                cart = Cart.objects.filter(cart_number=cart_no).first()
                if cart is not None:
                    cart.discount = None
                    cart.save()
                    success = True

    if success:
        messages.success(request, "Coupon removed from cart")
    else:
        messages.error(request, "Coupon is not removed from cart")

    return redirect('cart')


def save_cart(request):
    if request.method == "POST":
        cart_no = request.session.get('cart_number')
        cart = Cart.objects.filter(cart_number=cart_no).first()
        for key in request.POST:
            if key.startswith('sku'):
                sku = key.split('-')[1]
                quantity = int(request.POST.get(key))
                ci = CartItem.objects.filter(cart=cart, product__sku=sku).first()
                ci.qty = quantity
                ci.save()
            if key == 'shipping':
                shipping = request.POST.get('shipping')
                cart.shipping_method = shipping
        cart.save()
        messages.success(request, "Cart saved successfully")

def update_cart(request):

    save_cart(request)

    return redirect('cart')


def pay_now(request, sku):
    """
    Pays for a chosen product

    1. create a cart
    2. redirect cart to the checkout page
    """
    pass

@login_required
def checkout(request):
    """
    Cart Checkout
    """
    save_cart(request)

    template = 'cart/checkout.html'

    return render(request, template)