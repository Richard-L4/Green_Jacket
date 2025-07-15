from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from items.models import Item


def trolley_contents(request):
    """
    Retrieve the contents of the trolley from the session,
    calculate totals, delivery costs, and prepare the context
    dictionary for rendering in templates.
    """
    trolley_items = []
    total = 0
    item_count = 0
    trolley = request.session.get('trolley', {})

    # Iterate over items in the trolley session data
    for item_id, item_data in trolley.items():

        if isinstance(item_data, int):
            # Simple item without size variations
            item = get_object_or_404(Item, pk=item_id)
            total += item_data * item.price
            item_count += item_data
            trolley_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'item': item,
            })

        else:
            # Item with size variations
            item = get_object_or_404(Item, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * item.price
                item_count += quantity
                trolley_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'item': item,
                    'size': size,
                })

    # Calculate delivery cost based on total and free delivery threshold
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0')
        free_delivery_delta = Decimal('0')

    grand_total = delivery + total

    context = {
        'trolley_items': trolley_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
