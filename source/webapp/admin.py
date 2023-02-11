from django.contrib import admin
from webapp.models import Ads, Comment, Category



class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'created_at', 'description', 'category', 'price', 'status', 'status']
    search_fields = ['text', 'description']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Ads, AdAdmin)
admin.site.register(Category)
admin.site.register(Comment)
