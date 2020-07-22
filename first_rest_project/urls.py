from django.contrib import admin
from django.urls import path

from food.views import MainView, food_boxes_list, recipients_list, food_boxes_detail, recipient_detail

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('product-sets/', food_boxes_list, name='products_list'),
    path('product-sets/?min_price', food_boxes_list, name='products_list_min_price'),
    path('product-sets/?min_weight', food_boxes_list, name='products_list_min_weight'),
    path('product-sets/<pk>/', food_boxes_detail, name='product_detail'),
    path('recipients/', recipients_list, name='recipients_list'),
    path('recipients/<pk>/', recipient_detail, name='recipient-detail'),
    path('admin/', admin.site.urls),
]
