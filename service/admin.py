from django.contrib import admin

# Register your models here.

from .models import Product, Bin

#admin.site.register(Product)
admin.site.register(Bin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','id','cost']
    #fields = ['id']
    list_filter = ['cost']
    search_fields = ['title']

    #admin.site.register(Product, ProductAdmin)