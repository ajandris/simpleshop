# context_processors.py
from django.db.models import Sum
from .models import CartItem

def cart_item_count(request):

    cart_no = request.session.get('cart_number', {})
    if request.user.is_authenticated:
        count = CartItem.objects.filter(cart__owner_id=request.user, cart__cart_number=cart_no).\
            aggregate(total=Sum('qty'))['total'] or 0
    else:
        count = CartItem.objects.filter(cart__cart_number=cart_no).\
                    aggregate(total=Sum('qty'))['total'] or 0
    return {'cart_item_count': count}
