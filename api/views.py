from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *


class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsAPI(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        cat_param = self.request.query_params.get('cat')

        if cat_param:
            queryset = queryset.filter(category__slug=cat_param)

        return queryset


class ContactAPI(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SocialLinkAPI(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


