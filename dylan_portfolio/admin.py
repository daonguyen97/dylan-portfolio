from django.contrib import admin
from .models import Page
from .models import NavbarItem

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields= ('title',)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'url_link', 'status')
    list_editable = ('label', 'url_link', 'status')

admin.site.register(Page, PageAdmin)
admin.site.register(NavbarItem, NavbarItemAdmin)
