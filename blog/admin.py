from django.contrib import admin

from .models import BlogPost, Rating
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'num_ratings']

admin.site.register(BlogPost, BlogPostAdmin)