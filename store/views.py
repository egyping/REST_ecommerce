from django.http import HttpResponse # 2.2
from rest_framework.decorators import api_view # 2.3
from rest_framework.response import Response # 2.3
from .models import Collection, Product # 2.5 
from .serializers import ProductSerializer # 2.5 

from django.shortcuts import get_object_or_404 # 2.6

from rest_framework import status # 2.11
from logging import raiseExceptions # 2.11
from .serializers import CollectionSerializer # 2.12 
from django.db.models.aggregates import Count # 2.12

from rest_framework.views import APIView # 3.1
from rest_framework.generics import ListCreateAPIView # 3.2

# 3.2 Generic API view 
class ProducList(ListCreateAPIView):
    def get_queryset(self):
        return Product.objects.select_related('collection').all()

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raiseExceptions==True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# 3.1 API view - import 
# class ProducList(APIView):
#     def get(self, request):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raiseExceptions==True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# 3.1 ProductDetail
class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    


#2.12 collcetions list 
@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        # Adding attribute to object while query = annotate
        queryset = Collection.objects.annotate(products_count=Count('products')).all()
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raiseExceptions==True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 2.12 collections detail 
@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection.objects.annotate(products_count=Count('products')), pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # 2.11 
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
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
#     queryset = Product.objects.select_related('collection').all()
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






