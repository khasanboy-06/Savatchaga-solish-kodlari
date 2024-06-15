from django.urls import path
from .views import HomeView, ProductDetailView, CartDeteailView, delete_from_cart, category

app_name = 'cart'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:product_id>/', delete_from_cart, name='delete'),
    path('cart-detail/', CartDeteailView.as_view(), name='cart_detail'),
    path('category/<int:id>/', category, name='category'),
]