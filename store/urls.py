from django import views # 2.2
from django.urls import path  # 2.2
from . import views  # 2.2

urlpatterns = [
    # 2.2
    #path('products/', views.product_list), 

    # 2.4 int for integer and str for string
    #path('products/<int:id>/', views.product_detail),
    
    # 2.12 collections 
    path('collections/', views.collection_list),
    path('collections/<int:pk>/', views.collection_detail),
    
    # 3.1 APIView 
    path('products/', views.ProducList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),
]
