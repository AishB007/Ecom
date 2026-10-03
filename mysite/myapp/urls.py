from django.urls import include, path
from .views import index,product_detail

urlpatterns = [
    path("", index, name="index"),
    path("<slug:slug>/", product_detail, name="product_detail"),
]