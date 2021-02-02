from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product_name = serializers.CharField()
    product_description = serializers.CharField()

class CreateProductSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255, required=True)
    product_description = serializers.CharField(max_length=255, required=True, error_messages={"required": 'Campo requerido'} )

class StoreSerializer(serializers.Serializer):
    store_name = serializers.CharField()
    address = serializers.CharField()

class CreateStoreSerializer(serializers.Serializer):
    store_name = serializers.CharField(max_length=255, required=True)
    address = serializers.CharField(max_length=255, required=True, error_messages={"required": 'Campo requerido'} )

class StockSerializer(serializers.Serializer):
    qty = serializers.IntegerField()
    store_id = serializers.IntegerField()
    product_id = serializers.IntegerField()

class CreateStockSerializer(serializers.Serializer):
    qty = serializers.IntegerField(required=True, error_messages={"required": 'Campo requerido'})
    store_id = serializers.IntegerField(required=True, error_messages={"required": 'Campo requerido'})
    product_id = serializers.IntegerField(required=True, error_messages={"required": 'Campo requerido'})
