from django.contrib import admin

from main.models import *

# Create your views here.


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Company)
