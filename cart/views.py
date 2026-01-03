import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart, CartItem, Coupon, Shipping
from home.models import Profile, Address
from products.models import Product
from django.contrib import messages
from django.db.models import Sum, F
from decimal import Decimal, ROUND_HALF_UP

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def on_user_logged_in(sender, request, user, **kwargs):
    # This runs immediately after login
    request.session['just_logged_in'] = True


def view_cart(request):
    template = 'cart/cart.html'
    cart_no = request.session.get('cart_number')
    ctxt = dict()
    if cart_no:
        carts = Cart.objects.filter(cart_number=cart_no)
        shipping = Shipping.objects.all().order_by('price')
        cart_items = None
        if carts is None:
            if request.user.is_authenticated:
                carts = Cart.objects.filter(user=request.user)
                cart_items = CartItem.objects.filter(cart__owner_id=request.user.id)
        else:
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
    from .services import is_coupon_active_with_cart_minimum_value
    if request.method == "POST":
        if request.POST.get('coupon'):
            coupon = request.POST.get('coupon').strip().upper()
            coup = Coupon.objects.filter(code__iexact=coupon).first()
            if request.session.get('cart_number'):
                cart_no = request.session.get('cart_number')
                cart = Cart.objects.filter(cart_number=cart_no).first()
                if cart is not None and coup is not None:
                    cart.discount = coup
                    rez, msg = is_coupon_active_with_cart_minimum_value(cart)
                    if rez:
                        cart.save()
                        messages.success(request, "Coupon added to cart")
                    else:
                        messages.error(request, msg)

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


@login_required
def pay_now(request):
    """
    Pays for chosen products
    """
    return redirect('checkout')


def calculate_order(cart_no):
    """
    Calculates the order amounts
    """
    VAT = Decimal('20.00')
    cart = Cart
    try:
        cart = Cart.objects.get(cart_number=cart_no)
    except Cart.DoesNotExist:
        return {}

    shipping = None
    if cart.shipping_method is None:
        shipping = Shipping.objects.order_by('discount_threshold').first()
    else:
        shipping = Shipping.objects.filter(code=cart.shipping_method).first()

    cart_sub_total = CartItem.objects.filter(cart=cart).aggregate(
        total=Sum(F('price') * F('qty'))
    )

    ship_price = 5.00
    if Decimal(str(cart_sub_total['total'])) > Decimal(str(shipping.discount_threshold)):
        ship_price = shipping.price_discounted
    else:
        ship_price = shipping.price

    discount_amount = Decimal('0.00')
    if cart.discount_id is not None:
        disc = Coupon.objects.filter(id=cart.discount_id).first()
        if disc is not None:
            if disc.type == 'percent':
                discount_amount = disc.value * Decimal(str(cart_sub_total['total'])) / 100
            elif disc.type == 'amount':
                discount_amount = disc.value

    ord = dict()
    ord['cart_no'] = cart_no
    ord['shipping_price'] = ship_price
    ord['shipping_method_html'] = shipping.text_html
    ord['discount_value'] = Decimal(str(discount_amount)).quantize(
                                    Decimal("0.01"), rounding=ROUND_HALF_UP)
    ord['subtotal'] = Decimal(str(cart_sub_total['total']))
    ord['vat_percent'] = VAT
    ord['vat_amount'] = Decimal(str((Decimal(str(cart_sub_total['total'])) -
                                    Decimal(str(discount_amount))) * VAT / (100 - VAT))).quantize(
                                    Decimal("0.01"), rounding=ROUND_HALF_UP)

    ord['total'] = Decimal(str(ord.get('subtotal') - ord.get('discount_value') + ord.get('shipping_price'))).quantize(
                                    Decimal("0.01"), rounding=ROUND_HALF_UP)

    return ord


@login_required
def checkout(request):
    """
    Cart Checkout
    """
    save_cart(request)

    template = 'cart/checkout.html'

    user = get_user_model().objects.get(username=request.user.username)
    user_profile = get_object_or_404(Profile, owner=user)

    active_address = None
    active_address_id = None
    addresses = Address.objects.filter(profile=user_profile).order_by('-is_default')
    if request.method == 'POST':
        active_address_id = int(request.POST.get('active_address_id', '0'))

    print('aaa => ',active_address_id)

    if active_address_id:
        for address in addresses:
            if address.id == active_address_id:
                active_address = address
                break
    else:
        active_address = addresses[0]

    cart_no = request.session.get('cart_number')
    ctxt = dict()
    if cart_no:
        cart = Cart.objects.filter(cart_number=cart_no).first()
        shipping = Shipping.objects.filter(code=cart.shipping_method).first()
        if cart is not None:
            cart_items = CartItem.objects.filter(cart=cart)
            ord = calculate_order(cart_no)
            ctxt = dict(
                cart=cart,
                cart_items=cart_items,
                shipping_price=ord['shipping_price'],
                shipping_method_html=ord['shipping_method_html'],
                discount_value=ord['discount_value'],
                subtotal=ord['subtotal'],
                vat_percent=ord['vat_percent'],
                vat_amount=ord['vat_amount'],
                total=ord['total'],
                profile=user_profile,
                addresses=addresses,
                active_address=active_address
            )

    return render(request, template, context=ctxt)
