from django.urls import path

from authentication.views import login, logout, register

app_name = 'authentication'

urlpatterns = [
    # JSON endpoints consumed directly by the Flutter CookieRequest client.
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
