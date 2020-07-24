from django.shortcuts import render
from django.http import Http404
# Create your views here.


def index(request):
    """view to return home page"""
    return render(request, 'home/index.html')


def about(request):
    """view to render the about page"""
    return render(request, 'home/about.html')


def error_404_view(request):
    """
    server error 404 handler
    """
    if request.DoesNotExist:
        raise Http404
