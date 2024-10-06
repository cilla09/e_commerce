from django.urls import path
from main.views import show_main, create_product, show_xml, show_xml_by_id, show_json, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, show_profile_page, show_about_page, add_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product', create_product, name='create_product'),
    path('create_ajax', add_product_ajax, name='add_product_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>', delete_product, name='delete_product'),
    path('profile/', show_profile_page, name='profile'),
    path('about/', show_about_page, name='about')
]