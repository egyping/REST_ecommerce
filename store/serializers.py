from rest_framework import serializers

from store.models import Product # 2.5

from decimal import Decimal #2.7



# 2.5
class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField() # 2.5
    title = serializers.CharField(max_length=255) # 2.5
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2) # 2.5
    
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source= 'unit_price') # 2.8
    
    # 2.7
    # SerializerMethodField means you can write your own method 
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.5)