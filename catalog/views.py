from rest_framework.response import Response
from rest_framework.decorators import api_view
from catalog.models import Category, Product
from catalog.serializers import CategorySerializer, ProductSerializer
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from .filters import ProductFilter

@api_view(['GET'])
def category_list_view(request):
  serializer = CategorySerializer(Category.objects.all(), many=True)
  return Response(data=serializer.data)


# from rest_framework.views import APIView
# class CategoryView(APIView):
#   def get(self, request):
#     serializer = CategorySerializer(Category.objects.all(), many=True)
#     return Response(data=serializer.data)

class CategoryView(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ProductPagination(PageNumberPagination):
  page_size = 1 # Set default page to 1 for testing only
  page_size_query_param = 'page_size'
  def get_paginated_response(self, data):
    response = super().get_paginated_response(data)
    response.data['total'] = self.page.paginator.count
    response.data['pages'] = self.page.paginator.num_pages
    response.data['current_page'] = self.page.number
    return response

class ProductView(viewsets.ReadOnlyModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # pagination_class = PageNumberPagination
  pagination_class = ProductPagination
  filterset_fields = ['category__id']
  filterset_class = ProductFilter

from rest_framework.views import APIView
from rest_framework import status
class ProductDetailView(APIView):
  def get(self, request, product_id):
    show_error = request.query_params.get('show_error', 'false').lower() == 'true'
    product = Product.objects.filter(id=product_id).first()
    if product is not None:
      return Response(ProductSerializer(product).data)
    elif show_error:
      return Response(status=status.HTTP_404_NOT_FOUND, data="Product not found")
    else:
      return Response(status=status.HTTP_200_OK, data={})
    
# class ProductDetailView(generics.RetrieveAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
#   lookup_field = "id"
#   lookup_url_kwarg = "product_id"