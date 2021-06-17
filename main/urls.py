from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('add-product/', AddProduct.as_view(), name='add-product'),
    path('update-product/<int:pk>/', update_product, name='update-product'),
    path('list-product/', ProductListView.as_view(), name='list-product'),
    path('p/product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('pr/delete-product/<int:pk>/', DeleteRecipeView.as_view(), name='delete-product'),
    path('add-product-image/', AddProductImage.as_view(), name='add-image'),
    path('category/categories-detail/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),


]