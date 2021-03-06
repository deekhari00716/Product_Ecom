from django.urls import path
from . import views

app_name='item'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<slug:category_slug>', views.item_list, name='item_by_category'),
]
