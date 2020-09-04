from django.contrib import admin
from .models import Category, Tag, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time',
                    'modified_time', 'category', 'author']


# 把新增的 PostAdmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
