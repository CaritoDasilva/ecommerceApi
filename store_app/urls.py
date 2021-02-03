from django.urls import path
# from store_app.views import Papayas, PapayaDetails
from store_app.views import *
from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


# schema_view = get_swagger_view(title='CaritoEcommerce API')

urlpatterns = [
    # path('swagger-ui/', get_schema_view(
    #     title='Caritos API',
    # ), name='swagger-ui'),
      # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/products', getProducts),
    path('api/stores', getStores),
    path('api/stock', getStocks),
    path('api/stock/stores/<int:id_store>', getStockByStore),
    path('api/stock/products/<int:id_product>', getStockByProduct),
    path('api/stock/products/<int:id_product>/stores/<int:id_store>', getStockByStoreAndProduct),
    path('api/new/store', addStore),
    path('api/new/product', addProduct),
    path('api/new/stock', addStock)
]