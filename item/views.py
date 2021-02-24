from django.shortcuts import render, get_object_or_404
from.models import Category, Item


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    item = Item.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        item = item.filter(category=category)
    return render(request, 'item_list.html', {'categories':categories, 'category':category, 'item':item, })
