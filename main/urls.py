from django.urls import path

from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('account-detail/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('add-post/', AddPost.as_view(), name='add-post'),
    # path('update-product/<int:pk>/', update_product, name='update-product'),
    # path('list-product/', ProductListView.as_view(), name='list-product'),

    # path('pr/delete-product/<int:pk>/', DeleteRecipeView.as_view(), name='delete-product'),
    # path('up/p/add-image/<int:pk>', AddProductImage.as_view(), name='add-image'),
    # path('category/categories-detail/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),


]