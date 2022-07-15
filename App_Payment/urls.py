from django.urls import path
from App_Payment import views

app_name = 'App_Payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.payment, name='payment'),


]