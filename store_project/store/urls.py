from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name= "home_url"),
    path('product/<int:pk>/', ProductView.as_view(), name="product_detail_url"),
    path('cathegory/<int:pk>/', CathegoryView.as_view(), name="cathegory_detail_url"),
    path('save_order', save_order)
]
