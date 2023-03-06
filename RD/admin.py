import django.contrib
  # reg models
from .models import Customer
from .models import Product
from .models import Order
from .models import OrderItem
from .models import ShippingAddress

django.contrib.admin.site.register(Customer)
django.contrib.admin.site.register(Product)
django.contrib.admin.site.register(Order)
django.contrib.admin.site.register(OrderItem)
django.contrib.admin.site.register(ShippingAddress)