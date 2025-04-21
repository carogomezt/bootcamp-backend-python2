from django.urls import path
from .views import (
    ProductListView,
    CartDetailView,
    CartItemCreateView,
    CartItemUpdateView,
)

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("cart/<int:id>/", CartDetailView.as_view()),
    path("cart/<int:id>/add/", CartItemCreateView.as_view()),
    path("cart/<int:id>/update/", CartItemUpdateView.as_view()),
]
