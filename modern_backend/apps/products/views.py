from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)

from .models import Product
from .serializers import ProductSerializer



class ProductListView(ListApiView):
    
    queryset = Products.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    

class ProductRetrieveAPIView(RetrieveAPIView):
    
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductModelSerializer
    lookup_field = 'slug'

