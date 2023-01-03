from django.contrib import admin
from .models import userdata,products,latest_products

# Register your models here.
admin.site.register(userdata),
admin.site.register(products),
admin.site.register(latest_products),
