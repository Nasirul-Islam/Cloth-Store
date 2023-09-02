from django.shortcuts import render
from store.models import ProductsModel
from django.core.paginator import Paginator

def home(request):    
    sort_order = request.GET.get('sort')
    if sort_order == 'asc':
        items = ProductsModel.objects.filter(is_available=True).order_by('price')
    elif sort_order == 'desc':
        items = ProductsModel.objects.filter(is_available=True).order_by('-price')
    else:
        items = ProductsModel.objects.all()
        
    paginator = Paginator(items, 4) 
    page = request.GET.get('page') 
    items_on_page = paginator.get_page(page)
    context = {
        'products': items_on_page,
        'sort_order': sort_order,
    }
    return render(request, 'index.html', context)
