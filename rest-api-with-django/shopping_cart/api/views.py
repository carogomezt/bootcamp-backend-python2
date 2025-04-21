import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from .models import Product, Cart, CartItem


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        data = [model_to_dict(p) for p in products]
        return JsonResponse(data, safe=False)


class CartDetailView(View):
    def get(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)

        items_data = []
        for item in cart.items.select_related("product"):
            items_data.append(
                {
                    "product": item.product.name,
                    "price": float(item.product.price),
                    "quantity": item.quantity,
                    "total_price": float(item.total_price()),
                }
            )

        cart_data = {
            "id": cart.id,
            "created_at": cart.created_at,
            "total": cart.total(),
            "items": items_data,
        }
        return JsonResponse(cart_data, safe=False)


# Agregamos este decorador para evitar problemas por Cross Site Request Forgery Attacks (CSRF)
@method_decorator(csrf_exempt, name="dispatch")
class CartItemCreateView(View):
    def post(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)

        try:
            data = json.loads(request.body.decode("utf-8"))
            product_id = data.get("product_id")
            quantity = int(data.get("quantity", 1))
        except (KeyError, ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid input"}, status=400)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        else:
            item.quantity = quantity
        item.save()

        return JsonResponse(
            {
                "message": "Product added to cart",
                "cart_id": cart.id,
                "product": product.name,
                "quantity": item.quantity,
            }
        )


@method_decorator(csrf_exempt, name="dispatch")
class CartItemUpdateView(View):
    def patch(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)

        try:
            data = json.loads(request.body.decode("utf-8"))
            product_id = data.get("product_id")
            quantity = int(data.get("quantity", 1))
        except (KeyError, ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid input"}, status=400)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity = quantity

        cart_item.save()

        return JsonResponse(
            {
                "message": "Product updated in the cart",
                "cart_id": cart.id,
                "product": product.name,
                "quantity": cart_item.quantity,
            }
        )

    def delete(self, request, id):
        try:
            cart = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return JsonResponse({"error": "Cart not found"}, status=404)

        try:
            data = json.loads(request.body.decode("utf-8"))
            product_id = data.get("product_id")
        except (KeyError, ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Invalid input"}, status=400)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

        cart_item = CartItem.objects.get(cart=cart, product=product)

        cart_item.delete()

        return JsonResponse(
            {
                "message": "Card Item has been deleted",
            }
        )
