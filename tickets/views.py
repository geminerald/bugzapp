from django.shortcuts import render

# Create your views here.


def tickets(request):
    """
    Renders a page showing all currently open tickets
    """
    return render(request, 'tickets.html')