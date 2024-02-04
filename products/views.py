from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

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
    specials = None
    teams = None
    conditions = None
    current_filter = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'team':
                sortkey = 'team__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'league' in request.GET:
            leagues = request.GET['league'].split(",")
            products = products.filter(league__name__in=leagues)
            current_filter = f'League: {products[0].league.friendly_name}'
        
        if 'year' in request.GET:
            years = request.GET['year'].split(",")
            products = products.filter(year__in=years)
            current_filter = f'Year: {products[0].year}'

        if 'player_issue' in request.GET:
            products = products.filter(player_issue=True)
            specials = Product.objects.filter(player_issue=True)
            current_filter = 'Special category: Player issue'

        if 'signed' in request.GET:
            products = products.filter(signed=True)
            specials = Product.objects.filter(signed=True)
            current_filter = 'Special category: Signed'

        if 'team' in request.GET:
            teams = request.GET['team'].split(",")
            products = products.filter(team__name__in=teams)
            current_filter = f'Team: {products[0].team.friendly_name}'

        if 'condition' in request.GET:
            conditions = request.GET['condition'].split(",")
            products = products.filter(condition__name__in=conditions)
            current_filter = f'Condition: {products[0].condition.friendly_name}'
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search term entered")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_filter': current_filter,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)