from django.urls import path

from .views import *

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('account-detail/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('add-post/', AddPost.as_view(), name='add-post'),
    path('e/up/-p/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('pr/del/ete/post/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
    path('ma/p/st/de/ta/i/l/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('up/p/add-image/<int:pk>', AddProductImage.as_view(), name='add-image'),
    # path('category/categories-detail/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),


]