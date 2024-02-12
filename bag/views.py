from decimal import Decimal
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
import json

from products.models import Product

# Create your views here.

def view_bag(request):
    """ Render the bag contents page """

    return render(request, 'bag/bag.html')

# Add to bag (Code adapted from: https://www.youtube.com/watch?v=PgCMKeT2JyY)

def add_to_bag(request):

    # Get existing bag session if it exists
    bag = request.session.get('bag', {})

    # Calculate current bag total
    bag_total = 0
    product_count = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        bag_total += quantity * product.price
        product_count += quantity

    # Get product ID from JavaScript and lookup product details using model
    data = json.loads(request.body)
    add_product_id = data["id"]
    product = get_object_or_404(Product, pk=add_product_id)
    add_product_price = product.price

    # Add product if not already in bag
    if add_product_id in list(bag.keys()):
        pass
    else:
        bag_total += add_product_price
        product_count += 1
        bag[add_product_id] = 1
        messages.success(request, f'{product.name} added to bag')
    
    request.session['bag'] = bag

    return JsonResponse({"bag_total":bag_total, "product_count":product_count}, safe=False)

# Remove from bag

def remove_from_bag(request):

    # Get existing bag session if it exists
    bag = request.session.get('bag', {})

    # Calculate current bag total
    bag_total = 0
    product_count = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        bag_total += quantity * product.price
        product_count += quantity

    # Get product ID from JavaScript and lookup product details using model
    data = json.loads(request.body)
    del_product_id = data["id"]
    product = get_object_or_404(Product, pk=del_product_id)
    del_product_price = product.price

    # Remove product if in bag    
    if del_product_id in list(bag.keys()):
        bag_total -= del_product_price
        product_count -= 1
        bag.pop(del_product_id)
        messages.warning(request, f'{product.name} removed from bag')
    else:
        pass
    
    request.session['bag'] = bag

    return JsonResponse({"bag_total":bag_total, "product_count":product_count}, safe=False)