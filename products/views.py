from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.


def products(request):
    """
    Renders a page showing all currently open tickets
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products.html', context)
