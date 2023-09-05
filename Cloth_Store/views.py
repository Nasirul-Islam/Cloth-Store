from django.shortcuts import render
from store.models import ProductsModel
from django.core.paginator import Paginator
from store.models import ProductsModel
from .forms import SearchForm
from reviews.models import UserReviewsModel

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

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(query)
            results = ProductsModel.objects.filter(product_name__icontains=query)
            print(results)
            return render(request, 'index.html', {'products': results})
    else:
        form = SearchForm()
    # Average ratings 
    # reviews = UserReviewsModel.objects.filter(product = single_product).annotate(avg_rating=Avg('rating'))
    context = {
        'products': items_on_page,
        'sort_order': sort_order,
        'form': form,
    }
    return render(request, 'index.html', context)