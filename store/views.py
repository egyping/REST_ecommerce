
from django.http import HttpResponse # 2.2
from rest_framework.decorators import api_view # 2.3
from rest_framework.response import Response # 2.3
from .models import Product # 2.5 
from .serializers import ProductSerializer # 2.5 

from django.shortcuts import get_object_or_404 # 2.6

from rest_framework import status # 2.11
from logging import raiseExceptions # 2.11

# # 2.11 
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # take the data from the request and pass it to the serializer then validated 
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raiseExceptions==True)
        # make sure to add the missing fields at the product serializer "mandatory fields"
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#2.11 adding put methond to the detail 
@api_view(['GET', 'PUT', "DELETE"])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 2.6
# @api_view()
# def product_detail(request, id):
#     product = get_object_or_404(Product, pk=id)
#     serializer = ProductSerializer(product)
#     # serializer.data will convert product object to dictionary JSON 
#     return Response(serializer.data)




# # 2.6 
# @api_view()
# def product_list(request):
#     queryset = Product.objects.all()
#     serializer = ProductSerializer(queryset, many=True)
#     return Response(serializer.data)


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






