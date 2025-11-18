import datetime
import json

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import ProductForm
from .models import Product


def _product_to_dict(product: Product) -> dict:
    """Standardize how we expose Product rows to the Flutter client."""
    return {
        'id': str(product.id),
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'category': product.category,
        'thumbnail': product.thumbnail,
        'is_featured': product.is_featured,
        'stock': product.stock,
        'user_id': product.user_id,
        'created_at': product.created_at.isoformat() if product.created_at else None,
    }

# Create your views here.
@login_required(login_url='/login/')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(user=request.user)

    # products = Product.objects.all()
    context = {
        'npm' : '2406404781',
        'name': 'Muhammad Kaila Aidam Riyan',
        'class': 'PBP D',
        'liverpool_logo': 'https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg',
        'products': products,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login/')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

# Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

# def show_json(request):
#     product_list = Product.objects.all()
#     data = [
#         {
#             'id': str(product.id),
#             'name': product.name,
#             'price': product.price,
#             'description': product.description,
#             'category': product.category,
#             'thumbnail': product.thumbnail,
#             'is_featured': product.is_featured,
#             'stock': product.stock,
#             'user_id': product.user_id,
#         }
#         for product in product_list
#     ]
#     return JsonResponse(data, safe=False)

# Buka views.py yang ada pada direktori main dan buatlah dua fungsi baru yang menerima parameter request dan product_id dengan nama show_xml_by_id dan show_json_by_id.
# Buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada Product.
# product_item = Product.objects.filter(pk=product_id)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

# def show_json_by_id(request, product_id):
#    try:
#        product_item = Product.objects.get(pk=product_id)
#        json_data = serializers.serialize("json", [product_item])
#        return HttpResponse(json_data, content_type="application/json")
#    except Product.DoesNotExist:
#        return HttpResponse(status=404)
   

# REGISTER, LOGIN, AUTHENTICATION

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            
            # Return JSON response for AJAX requests
            if request.headers.get('Accept') == 'application/json':
                return JsonResponse({'success': True, 'message': 'Registration successful'})
            
            return redirect('main:login')
        else:
            # Return JSON error response for AJAX requests
            if request.headers.get('Accept') == 'application/json':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        
        # Return JSON response for AJAX requests
        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'success': True, 'message': 'Login successful'})
        
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        # Return JSON error response for AJAX requests
        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


# EDIT PRODUCT

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method == 'POST':
        # Check if user owns the product
        if product.user != request.user:
            if request.headers.get('Accept') == 'application/json':
                return JsonResponse({'error': 'Unauthorized'}, status=403)
            return HttpResponseRedirect(reverse('main:show_main'))
        
        product.delete()
        
        # Return JSON response for AJAX requests
        if request.headers.get('Accept') == 'application/json':
            return JsonResponse({'success': True, 'message': 'Product deleted successfully'})
        
        return HttpResponseRedirect(reverse('main:show_main'))
    
    return HttpResponseRedirect(reverse('main:show_main'))


# AJAX STUFF ====================================================

def show_json(request):
    """Expose every product so the Flutter "All" tab can hydrate its list."""
    product_list = Product.objects.all()
    data = [_product_to_dict(product) for product in product_list]
    return JsonResponse(data, safe=False)


def show_json_user(request):
    """Return only the authenticated user's items for the "My Products" tab."""
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'Authentication required.'}, status=401)

    product_list = Product.objects.filter(user=request.user)
    data = [_product_to_dict(product) for product in product_list]
    return JsonResponse(data, safe=False)


def show_json_by_id(request, product_id):
    """Single-product lookup used by detail screens and tests."""
    try:
        product_item = Product.objects.get(pk=product_id)
        return JsonResponse(_product_to_dict(product_item))
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name") or request.POST.get("title") or "")
    description = strip_tags(request.POST.get("description") or request.POST.get("content") or "")
    category = strip_tags(request.POST.get("category") or "")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user
    price = request.POST.get("price")
    stock = request.POST.get("stock")

    try:
        price = int(price)
    except (TypeError, ValueError):
        price = 0

    try:
        stock = int(stock)
    except (TypeError, ValueError):
        stock = 0

    new_product = Product(
        name=name,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
        price=price,
        stock=stock
    )
    new_product.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        
        # Check if user owns the product
        if product.user != request.user:
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        
        # Update product fields
        product.name = request.POST.get("name", product.name)
        product.price = request.POST.get("price", product.price)
        product.description = request.POST.get("description", product.description)
        product.category = request.POST.get("category", product.category)
        product.thumbnail = request.POST.get("thumbnail", product.thumbnail)
        product.is_featured = request.POST.get("is_featured") == 'on'
        product.stock = request.POST.get("stock", product.stock)
        
        product.save()
        return JsonResponse({'success': True, 'message': 'Product updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def get_product_json(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        return JsonResponse(_product_to_dict(product))
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


def proxy_image(request):
    """Fetch remote images server-side so Flutter can display HTTP-only URLs safely."""
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)

    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as exc:
        return HttpResponse(f'Error fetching image: {exc}', status=500)


@csrf_exempt
def create_product_flutter(request):
    """Accept JSON payloads from the Flutter form and persist them as Product rows."""
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'Authentication required.'}, status=401)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON payload.'}, status=400)

    name = strip_tags(data.get('name', '').strip())
    description = strip_tags(data.get('description', ''))
    category = strip_tags(data.get('category', ''))
    thumbnail = data.get('thumbnail', '')
    is_featured = data.get('is_featured', False)

    try:
        price = int(data.get('price', 0))
    except (TypeError, ValueError):
        price = 0

    try:
        stock = int(data.get('stock', 0))
    except (TypeError, ValueError):
        stock = 0

    if not name:
        return JsonResponse({'status': 'error', 'message': 'Product name is required.'}, status=400)

    new_product = Product(
        name=name,
        price=price,
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        stock=stock,
        user=request.user,
    )
    new_product.save()

    return JsonResponse({
        'status': 'success',
        'message': 'Product created successfully!',
        'data': _product_to_dict(new_product),
    }, status=201)