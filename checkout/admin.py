from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin class to display OrderLineItem instances
    within the Order admin.
    Only displays the lineitem_total field as read-only.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Order model.
    Includes inlines for related OrderLineItems and sets read-only fields,
    field order, list display fields, and default ordering.
    """
    inlines = (OrderLineItemAdminInline,)

    # Fields that cannot be edited through the admin
    readonly_fields = (
        'order_number', 'date', 'delivery_cost',
        'order_total', 'grand_total', 'original_trolley',
    )

    # Fields layout in the admin form view
    fields = (
        'order_number', 'user_profile', 'date', 'full_name',
        'email', 'phone_number', 'country', 'postcode',
        'town_or_city', 'street_address1', 'street_address2',
        'county', 'delivery_cost', 'order_total', 'grand_total',
        'original_trolley', 'stripe_pid',
    )

    # Fields to display in the list view
    list_display = (
        'order_number', 'date', 'full_name',
        'order_total', 'delivery_cost', 'grand_total',
    )

    # Orders displayed with most recent first
    ordering = ('-date',)


# Register the customized OrderAdmin with the admin site
admin.site.register(Order, OrderAdmin)
