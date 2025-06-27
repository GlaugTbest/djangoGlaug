from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Render the index page.
    """
    return render(request, 'app/index.html')

def pag2(request):
    """
    Render the second page.
    """
    return render(request, 'app/pag2.html')