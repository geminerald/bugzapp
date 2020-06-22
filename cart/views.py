from django.shortcuts import render

# Create your views here.


def cart(request):
    """
    Shows a user the cart page
    """

    return render(request, 'cart/cart.html')
