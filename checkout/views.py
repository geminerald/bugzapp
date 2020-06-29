from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm
from cart.contexts import cart_contents

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_js0eHzBCLVxtiXt9XLKiZuAh00Cvn2euvv',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
