from django.urls import path

from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('account-detail/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('add-post/', AddPost.as_view(), name='add-post'),

    path('pr/del/ete/post/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
    path('ma/p/st/de/ta/i/l/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchResultView.as_view(), name='search-results'),



]

