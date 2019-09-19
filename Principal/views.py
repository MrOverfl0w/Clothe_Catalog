from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
    
def item(request):
    return render(request, 'item.html')
    
def products(request):
    return render(request, 'products.html')