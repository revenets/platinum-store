from django.urls import path
from . import views

app_name = "platinum"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("oil/<int:pk>/", views.OilDetailView.as_view(), name="oil_detail"),
    path("brand/<int:pk>/", views.BrandDetailView.as_view(), name="brand_detail"),
    path("contacts/", views.contacts, name="contacts"),
    path("search/", views.search, name="search"),
    path("cart/", views.cart, name="cart"),
    path("add/order/", views.add_order, name="add_order"),
    path("process/order/", views.process_order, name="process_order"),


]