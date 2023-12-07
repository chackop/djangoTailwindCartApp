from django.urls import path

from . import views

urlpatterns = [
    path("items", views.CartItemListView.as_view(), name="cart.list"),
    path("items/<int:pk>", views.CartItemDetailView.as_view(), name="cart.detail"),
    path("items/new", views.CartItemCreateView.as_view(), name="cart.new"),
    path("items/<int:pk>/edit", views.CartItemUpdateView.as_view(), name="cart.update"),
    path(
        "items/<int:pk>/delete", views.CartItemDeleteView.as_view(), name="cart.delete"
    ),
]
