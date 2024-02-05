from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, League

# Create your views here.

def get_pages(page_number, items):
    """ Function to return paginated products using paginator """
    
    paginator = Paginator(items, 36)
            
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    
    return page_obj

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
    current_filter_display = None
    sort = None
    direction = None
    paginator = Paginator(products, 36)
    page_obj = paginator.page(1)
    page_num = 1
    
    if request.GET:

        if 'page' in request.GET:
            page_num = request.GET['page']
            page_obj = get_pages(page_num, products)

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
            page_obj = get_pages(page_num, products)
            
        if 'league' in request.GET:
            leagues = request.GET['league'].split(",")
            products = products.filter(league__name__in=leagues)
            page_obj = get_pages(page_num, products)
            current_filter = f'league={products[0].league.name}'
            current_filter_display = f'League: {products[0].league.friendly_name}'
            
        if 'year' in request.GET:
            years = request.GET['year'].split(",")
            products = products.filter(year__in=years)
            page_obj = get_pages(page_num, products)
            current_filter = f'year={products[0].year}'
            current_filter_display = f'Year: {products[0].year}'

        if 'player_issue' in request.GET:
            products = products.filter(player_issue=True)
            page_obj = get_pages(page_num, products)
            specials = Product.objects.filter(player_issue=True)
            current_filter = 'player_issue=true'
            current_filter_display = 'Special category: Player issue'

        if 'signed' in request.GET:
            products = products.filter(signed=True)
            page_obj = get_pages(page_num, products)
            specials = Product.objects.filter(signed=True)
            current_filter = 'signed=true'
            current_filter_display = 'Special category: Signed'

        if 'team' in request.GET:
            teams = request.GET['team'].split(",")
            products = products.filter(team__name__in=teams)
            page_obj = get_pages(page_num, products)
            current_filter = f'team={products[0].team.name}'
            current_filter_display = f'Team: {products[0].team.friendly_name}'

        if 'condition' in request.GET:
            conditions = request.GET['condition'].split(",")
            products = products.filter(condition__name__in=conditions)
            page_obj = get_pages(page_num, products)
            current_filter = f'condition={products[0].condition.name}'
            current_filter_display = f'Condition: {products[0].condition.friendly_name}'

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search term entered")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            page_obj = get_pages(page_num, products)
            current_filter = f'q={query}'
            current_filter_display = f'Search terms: {query}'
       
    current_sorting = f'{sort}_{direction}'
        
    context = {
        'products': products,
        'page_obj': page_obj,
        'search_term': query,
        'current_filter': current_filter,
        'current_filter_display': current_filter_display,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)