from django.shortcuts import render
# Create your views here.


def index(request):
    """view to return home page"""
    return render(request, 'home/index.html')

def about(request):
    """view to render the about page"""
    return render(request, 'home/about.html')
