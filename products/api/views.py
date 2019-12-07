from rest_framework import generics, mixins, permissions
# from rest_framework.generics import List
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View
from rest_framework.authentication import SessionAuthentication

from products.models import Products
from .serializers import ProductsSerializer, PriceSerializer, ColorSizeSerializer, ProductsAddSerializer

class ProductsListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = [SessionAuthentication]

    def get(self, request, format=None):
        qs = Products.objects.all()
        serializer = ProductsSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = Products.objects.all()
        serializer = ProductsSerializer(qs, many=True)
        return Response(serializer.data)


class ProductsAPIView(generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = ProductsSerializer

    def get_queryset(self):
        qs = Products.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class ProductsCreateAPIView( generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ProductsSerializer

class ProductsAddAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ProductsAddSerializer


class ProductsDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ProductsSerializer


class ProductsUpdateAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ProductsSerializer

class ProductsColorSizeAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ColorSizeSerializer


class PricesAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = PriceSerializer


class ProductsDeleteAPIView(generics.DestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Products.objects.all()
    serializer_class            = ProductsSerializer






