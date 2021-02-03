from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.decorators import api_view
# from django.http import HttpResponse
from django.views import View
from .models import Product, Store, Stock
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import *
from django.db.models import Sum
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Create your views here.

# class Papayas(View):
#     def get(self, request):        
#         return JsonResponse({'status': 'ok', 'papayas': list(Papaya.objects.values().all())})
#     def post(self, request):        
#         return JsonResponse({'status': 'ok'})
 
# class PapayaDetails(View):
#     def get(self, request, papaya_id):        
#         return JsonResponse({'status': 'ok'})
#     def put(self, request, papaya_id):        
#         return JsonResponse({'status': 'ok'})
#     def delete(self, request, papaya_id):        
#         return JsonResponse({'status': 'ok'})

#Trae todos los productos
@api_view()
def getProducts(request):
    products = Product.objects.all()
    return Response({'status': 'ok', 'products': ProductSerializer(products, many=True).data})

# Trae todas las tiendas
@api_view()
def getStores(request):
    stores = Store.objects.all()
    return Response({'status': 'ok', 'stores': StoreSerializer(stores, many=True).data})

# Trae stock de producto x tienda
@api_view()
def getStockByStoreAndProduct(request, id_product, id_store):
    productInStore = Stock.objects.filter(store=id_store, product=id_product)
    return Response({'status': 'ok', 'stock': StockSerializer(productInStore, many=True).data})

@api_view()
def getStocks(request):
    stocks = Stock.objects.all()
    return Response({'status': 'ok', 'stock': StockSerializer(stocks, many=True).data})

# Trae stock de producto sumando todas las tiendas
@api_view()
def getStockByProduct(request, id_product):
    product = Stock.objects.filter(product=id_product).aggregate(Sum('qty'))
    return Response({'status': 'ok', 'stock_product': product})

#Trae stock de tienda de todos sus producto disponibles
@api_view()
def getStockByStore(request, id_store):
    store_stock = Stock.objects.filter(store=id_store).aggregate(Sum('qty'))
    return Response({ 'store_stock': store_stock })


@extend_schema(
        request=ProductSerializer,
        responses={201: ProductSerializer},
        description='POST/Add product',
        parameters=[
            OpenApiParameter(  
                name='product_name',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='Nombre del producto',
                        value='Jeans Classic'
                    ),
                ],                
            ),
            OpenApiParameter(
                name='product_description',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='Descripción del producto',
                        value='Jeans de color negro con detalles bordados'
                    ),
                ],
            )
        ],
    )
@api_view(['POST'])
def addProduct(request):
    serializer = CreateProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    Product.objects.create(product_name=request.data['product_name'],
    product_description=request.data['product_description'])
    return Response({'status': 201, 'data': data})


@extend_schema(
        request=StoreSerializer,
        responses={201: StoreSerializer},
        description='POST/Add Store',
        parameters=[
            OpenApiParameter(  
                name='store_name',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='Nombre de la tienda',
                        value='Sucursal Las Condes'
                    ),
                ],                
            ),
            OpenApiParameter(
                name='address',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='Dirección de la tienda',
                        value='Metro apumanque'
                    ),
                ],
            )
        ],
    )
@api_view(['POST'])
def addStore(request):
    serializer = CreateStoreSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    Store.objects.create(store_name=request.data['store_name'],
    address=request.data['address'])
    return Response({'status': 200, 'data': data})

@extend_schema(
        request=StockSerializer,
        responses={201: StockSerializer},
        description='POST/Add Stock',
        parameters=[
            OpenApiParameter(  
                name='store_id',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='Id de la tienda',
                        value='1'
                    ),
                ],                
            ),
            OpenApiParameter(
                name='product_id',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='Id del producto',
                        value='1'
                    ),
                ],
            ),
            OpenApiParameter(
                name='qty',              
                examples=[
                    OpenApiExample(
                        'Example 1',
                        description='stock del producto',
                        value='200'
                    ),
                ],
            )
        ],
    )
@api_view(['POST'])
def addStock(request):
    serializer = CreateStockSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    id = request.data['store_id']
    store_id = Store.objects.get(id=id)
    print(id)
    isInStock = Stock.objects.filter(store=request.data['store_id'], product=request.data['product_id']).count()
    print('inStock', isInStock)
    if isInStock > 0:
        return Response({'message': 'Este registro de stock ya existe'}, status=409)
    else:
        Stock.objects.create(qty=request.data['qty'],
        store=store_id, product=Product.objects.get(id=request.data['product_id']))
        return Response({'status': 200, 'data': request.data})
        
        
#{"code": 200, "message": "OK", "description": "Se ha creado el usuario nuevo correctamente"}