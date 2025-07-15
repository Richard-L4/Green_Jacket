from django.shortcuts import (
    render, redirect, reverse,
    HttpResponse, get_object_or_404
)
from django.contrib import messages

from items.models import Item


def view_trolley(request):
    """Render the shopping trolley contents page."""
    return render(request, 'trolley/trolley.html')


def add_to_trolley(request, item_id):
    """
    Add a quantity of the specified product to the shopping trolley.

    Handles products with and without size variations.
    """
    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('item_size', None)
    trolley = request.session.get('trolley', {})

    if size:
        # Item has size variations
        if item_id in trolley:
            if size in trolley[item_id]['items_by_size']:
                trolley[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {item.name} quantity to '
                    f'{trolley[item_id]["items_by_size"][size]}'
                )
            else:
                trolley[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {item.name} to your trolley'
                )
        else:
            trolley[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {item.name} to your trolley'
            )
    else:
        # Item without size variations
        if item_id in trolley:
            trolley[item_id] += quantity
            messages.success(
                request,
                f'Updated {item.name} quantity to {trolley[item_id]}'
            )
        else:
            trolley[item_id] = quantity
            messages.success(
                request,
                f'Added {item.name} to your trolley'
            )

    request.session['trolley'] = trolley
    return redirect(redirect_url)


def adjust_trolley(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount.

    Removes the item if quantity is zero or less.
    """
    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('item_size', None)
    trolley = request.session.get('trolley', {})

    if size:
        # Adjust quantity for specific size
        if quantity > 0:
            trolley[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {item.name} quantity to '
                f'{trolley[item_id]["items_by_size"][size]}'
            )
        else:
            # Remove size from trolley
            del trolley[item_id]['items_by_size'][size]
            if not trolley[item_id]['items_by_size']:
                trolley.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {item.name} from your trolley'
            )
    else:
        # Adjust quantity for item without size
        if quantity > 0:
            trolley[item_id] = quantity
            messages.success(
                request,
                f'Updated {item.name} quantity to {trolley[item_id]}'
            )
        else:
            # Remove item from trolley
            trolley.pop(item_id)
            messages.success(
                request,
                f'Removed {item.name} from your trolley'
            )

    request.session['trolley'] = trolley
    return redirect(reverse('view_trolley'))


def remove_from_trolley(request, item_id):
    """
    Remove the item or specific size variation from the shopping trolley.

    Returns HTTP 200 on success, 500 on error.
    """
    item = get_object_or_404(Item, pk=item_id)

    try:
        size = request.POST.get('item_size', None)
        trolley = request.session.get('trolley', {})

        if size:
            # Remove specific size from trolley
            del trolley[item_id]['items_by_size'][size]
            if not trolley[item_id]['items_by_size']:
                trolley.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {item.name} from your trolley'
            )
        else:
            # Remove item without size from trolley
            trolley.pop(item_id)
            messages.success(request, f'Removed {item.name} from your trolley')

        request.session['trolley'] = trolley
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
