from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    bag_total = 0
    product_count = 0
    bag_skus = []
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        bag_total += quantity * product.price
        product_count += quantity
        bag_skus.append(product.sku)
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
        })

    if bag_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = bag_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - bag_total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + bag_total
    
    context = {
        'bag_items': bag_items,
        'bag_total': bag_total,
        'product_count': product_count,
        'bag_skus': bag_skus,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context