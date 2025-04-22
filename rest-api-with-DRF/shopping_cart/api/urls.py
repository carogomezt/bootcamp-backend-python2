from django.urls import path

from .views import (
    CartDetailView,
    CartItemCreateView,
    CartItemUpdateView,
    ProductListView,
)

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("cart/<int:id>/", CartDetailView.as_view()),
    path("cart/<int:id>/add/", CartItemCreateView.as_view()),
    path("cart/<int:id>/update/", CartItemUpdateView.as_view()),
]
