from django.contrib import admin
from .models import Item, Category, SavedItem, Review
from django.utils.html import format_html


# Inline review display for Items
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    fields = ('user', 'review_text', 'created_at')
    readonly_fields = ('created_at',)


# Items admin with inline reviews and image preview
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image_tag',
    )
    ordering = ('sku',)
    inlines = [ReviewInline]

    def image_tag(self, obj):
        if obj.featured_image:
            img = obj.featured_image.url
            return format_html('<img src="{}" width="50" />', img)
        return "-"
    image_tag.short_description = 'Image'


# Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


# SavedGoods admin
@admin.register(SavedItem)
class SavedItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'saved_at')
    search_fields = ('user__username', 'item__name')
    list_filter = ('saved_at',)


# Review admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'created_at')
    search_fields = ('user__username', 'item__name', 'review_text')
    list_filter = ('created_at',)


# Register Goods and Category using the defined admin classes
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
