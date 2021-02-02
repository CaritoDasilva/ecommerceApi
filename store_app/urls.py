from django.urls import path
# from store_app.views import Papayas, PapayaDetails
from store_app.views import *
 
urlpatterns = [
    # path( 'papaya', Papayas.as_view() ),    
    # path( 'papaya/<int:papaya_id>', PapayaDetails.as_view() )
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