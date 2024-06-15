from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Products, Cart, Category


class HomeView(View):
    def get(self, request):
        products = Products.objects.filter(in_stock=True)
        cart = Cart.objects.count()
        return render(request, 'cart/home.html', context={"products":products, "cart":cart})

class ProductDetailView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        cart = Cart.objects.count()
        return render(request, 'cart/detail.html', context={"product":product, "cart":cart})
    

    def post(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        quantity = int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart = Cart.objects.filter(product=product).first()
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart()
            cart.product = product
            cart.quantity = quantity
            cart.save()
        return redirect('cart:home')
    
class CartDeteailView(View):
    def get(self, request):
        products = Cart.objects.all()
        return render(request, 'cart/cart_detail.html', context={"products":products})
    

def delete_from_cart(request, product_id):
    cart = get_object_or_404(Cart, id=product_id)
    cart.delete()
    return redirect('cart:home')


def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"products":products, "categories":categories})