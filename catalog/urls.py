from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ContactsView,
    ContactFormView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/new/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path(
        "products/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "products/delete/<int:pk>", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("contact/", ContactFormView.as_view(), name="contact"),
]
