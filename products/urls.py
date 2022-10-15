from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.admin_add_product, name='admin_add_product'),
    path('edit/<int:product_id>/', views.admin_edit_product, name='admin_edit_product'),
    path('delete/<int:product_id>/', views.admin_delete_product, name='admin_delete_product'),
]
