from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Cart, CartItem, Product
from .serializers import CartItemSerializer, CartSerializer, ProductSerializer


# Create your views here.
# class ProductListView(GenericAPIView):
class ProductListView(APIView):
    serializer_class = ProductSerializer
    # pagination_class = PageNumberPagination

    def get_queryset(self):
        return Product.objects.all()

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )
        # return self.get_paginated_response({"status": "success", "data": self.paginate_queryset(serializer.data)})


class CartDetailView(APIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.all()

    def get(self, request, id=None):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = CartSerializer(cart)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )


class CartItemCreateView(APIView):
    serializer_class = CartItemSerializer

    def post(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Product added to cart"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CartItemUpdateView(APIView):
    serializer_class = CartItemSerializer

    def patch(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product_id = request.data.get("product_id")

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        serializer = CartItemSerializer(cart_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, id=None):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(
                {"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND
            )

        product_id = request.data.get("product_id")

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
            )

        item = get_object_or_404(CartItem, cart=cart, product=product)
        item.delete()
        return Response(
            {"status": "success", "data": "Item Deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
