from django.contrib import admin
from .models import Contact, FreeQuote,Subscribe
admin.site.site_header = 'StartUpCentre Management'
admin.site.index_title = 'Customization Functionality'

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'phone_number', 'message')
    list_filter = ('created_at',)
    
@admin.register(FreeQuote)
class FreeQuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'select_service', 'created_at')
    search_fields = ('name', 'email', 'select_service', 'message')
    list_filter = ('select_service', 'created_at')
    
@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email','created_at')
    list_filter = ('email', 'created_at')