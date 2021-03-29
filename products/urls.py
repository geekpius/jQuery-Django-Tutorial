from django.urls import path
from products.views import ProductView, ProductCategoryView

app_name = "products"

urlpatterns = [
    path('', ProductView.as_view(), name="products"), 
    path('<str:category>', ProductCategoryView.as_view(), name="products_category"), 
]