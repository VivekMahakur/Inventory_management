from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('inventory/', views.inventory, name='inventory'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),  # Ensure product_id is passed
    path('calculator/', views.calculator, name='calculator'),
    path('add_product/', views.add_product, name='add_product'),  # Add product URL
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),  # Delete product URL
]
