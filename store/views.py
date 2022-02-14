from django.http import HttpResponse # 2.2
from rest_framework.decorators import api_view # 2.3
from rest_framework.response import Response # 2.3
from .models import Product # 2.5 
from .serializers import ProductSerializer # 2.5 

from django.shortcuts import get_object_or_404 # 2.6


# 2.6
@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    # serializer.data will convert product object to dictionary JSON 
    return Response(serializer.data)

# # 2.6 
@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


# 2.5
# @api_view()
# def product_detail(request, id):
#     product = Product.objects.get(pk=id)
#     serializer = ProductSerializer(product)
#     # serializer.data will convert product object to dictionary JSON 
#     return Response(serializer.data)


# 2.4
# @api_view()
# def product_detail(request, id):
#     return Response(id)

# 2.3 
# @api_view()
# def product_list(request):
#     return Response('ok')


# 2.2
# def product_list(request):
#     return HttpResponse('ok')






