from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Keeps a running count of items in the cart if the user leaves before
    checking out. Returns this in a context which is accessible throughout
    the site.
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count
    }
    return context
