from django.contrib import admin

# Register your models here.
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "image_url", "remark", "is_show", "orders", "is_deleted"]
    list_editable = ["is_show", "orders", "is_deleted"]
    search_fields = ["title", "link", "image_url", "remark"]
    list_filter = ["is_show", "is_deleted"]

admin.site.register(Banner, BannerAdmin)

