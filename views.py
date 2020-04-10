from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import Category, Product

# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)
    return render(request,'product/list.html',
                {'category':category,'categories':categories,'product':product})


def product_detail(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html',{'product':product, 'cart_product_form': cart_product_form})


# #just test
# def product_list2(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     product = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         product = product.filter(category=category)
#     return render(request,'product/list.html',
#                 {'category':category,'categories':categories,'product':product})

# def product_detail2(request, product_id, slug):
#     product = get_object_or_404(Product, id=product_id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'product/detail.html',{'product':product, 'cart_product_form': cart_product_form})
