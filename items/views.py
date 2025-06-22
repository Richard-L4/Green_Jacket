from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Item, Review, SavedItem, Category
from .forms import ItemForm, ReviewForm
from django.http import JsonResponse


def all_items(request):
    """ Show all items, including sorting, search, and category filter """

    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    current_category = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            current_category = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error
                (request, "You didn't enter any search criteria!")
                return redirect('items')

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'
    all_categories = Category.objects.all()

    return render(request, 'items/items.html', {
        'items': items,
        'search_term': query,
        'current_categories': current_category,
        'categories': all_categories,
        'current_sorting': current_sorting,
    })


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    reviews = item.reviews.select_related('user')
    
    saved = (
        request.user.is_authenticated and
        SavedItem.objects.filter(
            user=request.user,
            item=item
        ).exists()
    )

    review_form = ReviewForm()

    context = {
        'item': item,
        'reviews': reviews,
        'saved': saved,
        'review_form': review_form,
    }
    return render(request, 'items/item_detail.html', context)


@staff_member_required
def add_item(request):
    """ Add a item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(
                request,
                'Failed to add item. Please ensure the form is valid.'
            )
    else:
        form = ItemForm()

    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@staff_member_required  # Only staff/superusers can access this
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully!')
            return redirect('item_detail', pk=item.id)
    else:
        form = ItemForm(instance=item)

    return render(request, 'items/edit_item.html', {
        'form': form,
        'item': item,
    })


@staff_member_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('items')  # or wherever you want after deleting
    # If GET, you can optionally show a confirmation page or just redirect
    return redirect('items')


@login_required
def add_review(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.item = item
        review.save()
    return redirect('item_detail', pk=pk)


@login_required
def edit_review(request, pk, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'item_id': pk})


@login_required
def delete_review(request, pk, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
    return redirect('item_detail', pk=pk)


@login_required
def toggle_save_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    saved_obj, created = SavedItem.objects.get_or_create(
        user=request.user, item=item)
    if not created:
        saved_obj.delete()
        return JsonResponse({'saved': False})
    else:
        return JsonResponse({'saved': True})