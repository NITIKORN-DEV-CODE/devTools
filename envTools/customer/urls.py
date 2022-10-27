from django.urls import path
from customer import views

urlpatterns = [
    path('customer', views.customerApi_customer),
    path('customer/<int:pk>', views.customerApi_customer),
    path('order', views.orderApi_order),
    path('order/<int:pk>', views.orderApi_order),
    path('orderproduct', views.orderApi_orderproduct),
    path('product', views.productApi_product),
    path('product/<int:pk>', views.productApi_product),
    path('profile', views.customerApi_profile),
    path('imageslip', views.productApi_imageslip),
    path('imageslip/<int:pk>', views.productApi_imageslip),
    path('address', views.productApi_address),
    path('address/<int:pk>', views.productApi_address),
    ]
