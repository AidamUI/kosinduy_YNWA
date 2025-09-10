from django.shortcuts import render
from .models import Item

# Create your views here.
def show_main(request):
    items = Item.objects.all()
    context = {
        'npm' : '2406404781',
        'name': 'Muhammad Kaila Aidam Riyan',
        'class': 'PBP D',
        'liverpool_logo': 'https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg',
        'items': items,
    }

    return render(request, "main.html", context)