from django.contrib import admin
from .models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
