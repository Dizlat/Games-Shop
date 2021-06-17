from django.contrib import admin

from main.models import *

# Create your views here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
