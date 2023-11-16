from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Product, Cathegory, Order
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin


def build_template(lst,col):
    return [lst[i:i + col] for i in range(0,len(lst),col)]


class CathegoryMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cathegory_list"] = Cathegory.objects.all()
        return context


class HomeView(CathegoryMixin, ListView):
    model = Product

    def get_queryset(self):
        search_querry = self.request.GET.get('search',None)
        if search_querry:
            return self.model.objects.filter(title__icontains=search_querry)  
        return self.model.objects.all()


class ProductView(CathegoryMixin, DetailView):
    model = Product


class CathegoryView(CathegoryMixin, DetailView):
    model = Cathegory


def save_order(request):
    cathegory_list = Cathegory.objects.all()
    product = Product.objects.get(id=request.POST["product_id"])
    order = Order()
    order.name=request.POST["user_name"]
    order.email=request.POST["user_email"]
    order.product = product
    order.save()
    return render(request, "store/order.html", context={"product": product, "user_name": order.name, "cathegory_list": cathegory_list   })


