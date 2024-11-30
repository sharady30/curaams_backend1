from django.contrib import admin
from .models import Disease

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Columns to display in the admin list view
    search_fields = ('name', 'category')  # Add search functionality

admin.site.register(Disease, DiseaseAdmin)
