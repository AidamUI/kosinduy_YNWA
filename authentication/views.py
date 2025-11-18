import json

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    """Handle credential check for Flutter CookieRequest clients."""
    # Flutter sends credentials via form-encoded fields, so read them straight off POST.
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return JsonResponse({
            "status": False,
            "message": "Username and password are required."
        }, status=400)

    user = authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth_login(request, user)
        return JsonResponse({
            "username": user.username,
            "status": True,
            "message": "Login successful!"
        }, status=200)

    return JsonResponse({
        "status": False,
        "message": "Login failed, please check your username or password."
    }, status=401)


@csrf_exempt
def register(request):
    """Register a new user via JSON payload."""
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            "status": False,
            "message": "Invalid JSON payload."
        }, status=400)

    # Mirror the Flutter register form fields so both platforms share the same validation.
    username = data.get('username')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not all([username, password1, password2]):
        return JsonResponse({
            "status": False,
            "message": "All fields are required."
        }, status=400)

    if password1 != password2:
        return JsonResponse({
            "status": False,
            "message": "Passwords do not match."
        }, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username already exists."
        }, status=400)

    user = User.objects.create_user(username=username, password=password1)
    user.save()

    return JsonResponse({
        "username": user.username,
        "status": "success",
        "message": "User created successfully!"
    }, status=200)


@csrf_exempt
def logout(request):
    # Sending the username back helps Flutter personalize SnackBar copy.
    username = request.user.username if request.user.is_authenticated else ""
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except Exception:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)
