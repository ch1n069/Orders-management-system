from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')



def products(request):
    return render(request, 'accounts/products.html')
    