from django.contrib import admin
from .models import Books

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year', 'status')
    search_fields = ('title', 'author') 
    list_filter = ('status', 'year')
    ordering = ('-year',)
