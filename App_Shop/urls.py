from django.urls import path
from App_Shop import views

app_name = 'App_Shop'

urlpatterns = [
    path('', views.product_list, name='home'),
    path('<slug:category_slug>', views.product_list, name='product_by_category'),
    path('product_detail/<pk>/', views.ProductDetail.as_view(), name="product_detail"),

]