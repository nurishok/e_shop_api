from rest_framework import viewsets

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        parent_slug = self.request.query_params.get('parent')
        if parent_slug is not None:
            parent_slug = parent_slug.rstrip('/')
            queryset = queryset.filter(parent_id=parent_slug)
        return queryset


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {'request': self.request}

# TODO related products in category details
# TODO add pagination
# TODO add filtering
# TODO add_to_cart
# TODO add views for images
