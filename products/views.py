from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, League

# Create your views here.

def all_products(request):
    """ View to return all products, including sorting and search queries """
    
    products = Product.objects.all()
    query = None
    leagues = None
    years = None
    player_issue = False
    signed = False

    if request.GET:
        if 'league' in request.GET:
            leagues = request.GET['league'].split(",")
            products = products.filter(league__name__in=leagues)
            leagues = League.objects.filter(name__in=leagues)
        
        if 'year' in request.GET:
            years = request.GET['year'].split(",")
            products = products.filter(year__in=years)
            years = Product.objects.filter(year__in=years)

        if 'player_issue' in request.GET:
            products = products.filter(player_issue=True)

        if 'signed' in request.GET:
            products = products.filter(signed=True)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search term entered")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_leagues': leagues,
    }

    return render(request, 'products/products.html', context)