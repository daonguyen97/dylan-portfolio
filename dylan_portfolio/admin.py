from django.contrib import admin
from .models import Page
from .models import NavbarItem
from .models import File

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields= ('title',)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'url_link', 'status')
    list_editable = ('label', 'url_link', 'status')
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_shared')
    list_editable = ('name', 'is_shared')


admin.site.register(Page, PageAdmin)
admin.site.register(NavbarItem, NavbarItemAdmin)
admin.site.register(File)
