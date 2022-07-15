from django.urls import path
from App_Order import views

app_name = 'App_Order'

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove_from_cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase_cart/<int:pk>/', views.increase_cart, name='increase_cart'),
    path('decrease_cart/<int:pk>/', views.decrease_cart, name='decrease_cart'),


]