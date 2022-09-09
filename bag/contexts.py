from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total_sum = 0
    product_number = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total_sum += quantity * product.price
        product_number += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total_sum < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total_sum * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total_sum
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total_sum
    
    context = {
        'bag_items': bag_items,
        'total_sum': total_sum,
        'product_number': product_number,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context