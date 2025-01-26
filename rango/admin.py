from django.contrib import admin
from rango.models import Category, Page, UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    
    fieldsets = [
        (None,      {'fields': ['title', 'category', 'url']}),
        ('Metrics', {'fields': ['views']}),
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
