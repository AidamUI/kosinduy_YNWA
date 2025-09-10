from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()
    context = {
        'npm' : '2406404781',
        'name': 'Muhammad Kaila Aidam Riyan',
        'class': 'PBP D',
        'liverpool_logo': 'https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg',
        'products': products,
    }

    return render(request, "main.html", context)