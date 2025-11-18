from django.urls import path

from main.views import (
    add_product,
    add_product_entry_ajax,
    create_product_flutter,
    delete_product,
    edit_product,
    edit_product_ajax,
    get_product_json,
    login_user,
    logout_user,
    proxy_image,
    register,
    show_json,
    show_json_by_id,
    show_json_user,
    show_main,
    show_product,
    show_xml,
    show_xml_by_id,
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/user/', show_json_user, name='show_json_user'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('add_product/', add_product, name='add_product'),
    path('product/<int:id>/', show_product, name='show_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),
    path('add_product_entry_ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),  # New URL pattern for AJAX product creation
    path('edit_product_ajax/<int:id>/', edit_product_ajax, name='edit_product_ajax'),  # AJAX edit endpoint
    path('get_product_json/<int:id>/', get_product_json, name='get_product_json'),  # Get product JSON data
    # Flutter integration endpoints bridge the mobile form + media proxy to Django.
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]