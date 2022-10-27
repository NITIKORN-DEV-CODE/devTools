from django.contrib import admin
from customer.models import Customer, Order, Address, OrderProduct, ImageSlip, Product, ImageProduct

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderProduct)
admin.site.register(ImageSlip)
admin.site.register(Product)
admin.site.register(ImageProduct)
