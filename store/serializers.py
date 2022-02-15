from dataclasses import fields
from rest_framework import serializers

from store.models import Collection, Product # 2.5

from decimal import Decimal #2.7


# 2.11 > same like 2.10 just add the missing fields
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection', 'price_with_tax',
                  'slug', 'inventory', 'description',]
    #custom field
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.5)
    
# 2.10
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id', 'title', 'unit_price', 'collection', 'price_with_tax',]
#     #custom field
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.5)

# 2.10
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']
    
        
# 2.9 
# class CollectionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


# 2.5
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField() # 2.5
#     title = serializers.CharField(max_length=255) # 2.5
#     # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2) # 2.5
    
#     price = serializers.DecimalField(max_digits=6, decimal_places=2, source= 'unit_price') # 2.8
    
#     # 2.7
#     # SerializerMethodField means you can write your own method 
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     def calculate_tax(self, product: Product):
#         return product.unit_price * Decimal(1.5)
    
#     # 2.9
#     collection = CollectionSerializer()