from django.urls import path
from . import views


urlpatterns = [
    path('create_store/', views.create_store_view, name='create_store'),
    path('', views.all_store_view, name='home'),
    path('view_store/<int:id>/', views.detail_store_view, name='view_store'),
    path('delete_store/<int:id>/', views.deleteStore, name="delete_store"),
]
