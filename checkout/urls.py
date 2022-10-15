from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'payment_success/<order_number>',
        views.payment_success, name='payment_success'),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
