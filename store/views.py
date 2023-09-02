from django.shortcuts import render, get_object_or_404
from .models import ProductsModel
from category.models import ProductsCategory
from django.core.paginator import Paginator

# Create your views here.
def store(request, category_slug=None):
    products = None
    if category_slug:
        category = get_object_or_404(ProductsCategory, slug = category_slug)
        size = request.GET.get('size')
        color = request.GET.get('color')
        if size and color:
            products = ProductsModel.objects.filter(is_available=True, category=category, size=size, color=color)
        elif size:
            products = ProductsModel.objects.filter(is_available=True, category=category, size=size)
        elif color:
            products = ProductsModel.objects.filter(is_available=True, category=category, color=color)
        else:
            products = ProductsModel.objects.filter(is_available=True, category=category)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
    else:
        products = ProductsModel.objects.filter(is_available=True)
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
    categorys = ProductsCategory.objects.all()
    context = {'products':page_product, 'categorys':categorys}
    return render(request, 'store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = ProductsModel.objects.get(slug=product_slug, category__slug = category_slug)
    return render(request, 'product-detail.html', {'product': single_product})

