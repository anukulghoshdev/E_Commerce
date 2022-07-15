from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from App_Shop.models import Product, Category

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
    return render(request, 'App_Shop/home.html',
                  context={'categories': categories, 'category': category, 'products': product, })


class ProductDetail(LoginRequiredMixin, DetailView):  # by_default = object
    model = Product
    context_object_name = 'product'
    template_name = 'App_Shop/product_detail.html'
