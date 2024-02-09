from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from products.models import Product

# Create your views here.

def view_bag(request):
    """ Render the bag contents page """

    return render(request, 'bag/bag.html')

# Add to bag (Code adapted from: https://www.youtube.com/watch?v=PgCMKeT2JyY)

def add_to_bag(request):
    
    data = json.loads(request.body)
    product_id = data["id"]

    bag = request.session.get('bag', {})
    if product_id in list(bag.keys()):
        pass
    else:
        bag[product_id] = 1

    request.session['bag'] = bag
 
    return JsonResponse({"id":product_id}, safe=False)