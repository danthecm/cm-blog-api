from django.contrib import admin
from .models import Blog, BlogTag, BlogComment

# Register your models here.
admin.site.register((Blog, BlogTag, BlogComment))
