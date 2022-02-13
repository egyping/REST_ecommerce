from django import views # 2.2
from django.urls import path  # 2.2
from . import views  # 2.2

urlpatterns = [
    path('products/', views.product_list), # 2.2
    # 2.4 int for integer and str for string
    path('products/<int:id>/', views.product_detail), # 2.4
]
