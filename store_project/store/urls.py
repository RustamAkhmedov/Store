from django.urls import path
from .views import product_list, cathegories_list, product_detail, cathegory_detail, save_order

urlpatterns = [
    path("", product_list, name= "home_url"),
    path('cats/', cathegories_list, name = "cathegory_list_url"),
    path('product/<int:product_id>/', product_detail, name="product_detail_url"),
    path('cathegory/<int:cathegory_id>/', cathegory_detail, name="cathegory_detail_url"),
    path('save_order', save_order)
]

