from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'drink_type', 'price')
    list_filter = ('drink_type', 'date')
    search_fields = ('name', 'memo')
