from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages

from items.models import Item


def view_trolley(request):
    """ A view that renders the trolley contents page """

    return render(request, 'trolley/trolley.html')


def add_to_trolley(request, item_id):
    """ Add a quantity of the specified product to the shopping trolley """

    item = get_object_or_404(Item, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    trolley = request.session.get('trolley', {})

    if size:
        if item_id in list(trolley.keys()):
            if size in trolley[item_id]['items_by_size'].keys():
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
        if item_id in list(trolley.keys()):
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
    Adjust the quantity of the specified product to the specified amount
    """

    item = get_object_or_404(Item, pk=item_id)

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'item_size' in request.POST:
        size = request.POST['item_size']
    trolley = request.session.get('trolley', {})
    if size:
        if quantity > 0:
            trolley[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {item.name} quantity to '
                f'{trolley[item_id]["items_by_size"][size]}'
            )
        else:
            del trolley[item_id]['items_by_size'][size]
            if not trolley[item_id]['items_by_size']:
                trolley.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {item.name} from your trolley'
            )
    else:
        if quantity > 0:
            trolley[item_id] = quantity
            messages.success(
                request,
                f'Updated {item.name} quantity to {trolley[item_id]}'
            )
        else:
            trolley.pop(item_id)
            messages.success(
                request,
                f'Removed {item.name} from your trolley'
            )

    request.session['trolley'] = trolley
    return redirect(reverse('view_trolley'))


def remove_from_trolley(request, item_id):
    """ Remove the item from the shopping trolley """

    item = get_object_or_404(Item, pk=item_id)

    try:
        size = None
        if 'item_size' in request.POST:
            size = request.POST['item_size']
        trolley = request.session.get('trolley', {})

        if size:
            del trolley[item_id]['items_by_size'][size]
            if not trolley[item_id]['items_by_size']:
                trolley.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {item.name} from your trolley'
            )
        else:
            trolley.pop(item_id)
            messages.success(request, f'Removed {item.name} from your trolley')

        request.session['trolley'] = trolley
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)