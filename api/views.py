from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from django.db.models import Q

from .utils import send_email


class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsAPI(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        cat_param = self.request.query_params.get('product_slug')
        q = self.request.query_params.get('q')
        discount = self.request.query_params.get('discount')
        category_slug = self.request.query_params.get("category_slug")

        if category_slug:
            queryset = Product.objects.filter(category__slug=category_slug)
        elif cat_param:
            queryset = queryset.filter(slug=cat_param)
        elif q:
            queryset = queryset.filter(
                Q(name__icontains=q)
            )
        elif discount:
            queryset = queryset.filter(discount__gte=1)

        return queryset


class ContactAPI(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SocialLinkAPI(generics.ListAPIView):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class SupportAPI(APIView):
    def post(self, request):
        print(request.data)
        return Response({})


class AboutAPI(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class SliderAPI(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
