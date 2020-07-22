from django.shortcuts import render, redirect, reverse

# Create your views here.


def cart(request):
    """
    Shows a user the cart page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Takes an item ID and adds that item to the cart which can then be accessed
    via the contexts.py file in this app throughout the site.
    """
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(reverse('checkout'))
