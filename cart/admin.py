from django.contrib import admin

from . import models

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ("title", "price")


admin.site.register(models.CartItem, CartAdmin)
