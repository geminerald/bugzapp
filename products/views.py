from django.shortcuts import render
from .models import Product

# Create your views here.


def products(request):
    """
    Renders a page showing all currently open tickets
    """
    products = Product.objects.all().order_by('price')

    context = {
        'products': products,
    }

    return render(request, 'products.html', context)
