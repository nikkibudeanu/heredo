from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('products_management/',
         views.products_management, name='products_management'),
]
