from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'description')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')

