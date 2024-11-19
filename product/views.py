from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.shortcuts import get_object_or_404
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
# Create your views here.


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        print(serializer.data)
        return Response({"products": serializer.data},
                        status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetProductByIdView(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=204)


class AddImageArrayToProduct(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, pk):
        """
        Endpoint to upload multiple images for a product.
        """
        product = get_object_or_404(Product, pk=pk)

        if 'images' not in request.FILES:
            return Response({"error": "No images provided."},
                            status=status.HTTP_400_BAD_REQUEST)

        images = request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return Response({"message": "Images uploaded successfully."},
                        status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        """
        Endpoint to retrieve all images for a product.
        """
        product = get_object_or_404(Product, pk=pk)
        images = ProductImage.objects.filter(product=product)
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
