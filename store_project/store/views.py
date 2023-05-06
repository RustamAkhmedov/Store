from django.shortcuts import render
from .models import Product, Cathegory

def build_template(lst,col):
    return [lst[i:i + col] for i in range(0,len(lst),col)]


def product_list(request):
    search_querry = request.GET.get('search',None)
    if search_querry:
        products = Product.objects.filter(title__icontains=search_querry)
    else:  
        products = Product.objects.all()
    return render(request, "store/product_list.html", context={"product_list": build_template(products, 3)})


def cathegories_list(request):
    cathegories = Cathegory.objects.all()
    return render(request, "store/cathegories_list.html", context={"cathegories": cathegories})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "store/product_detail.html", context={"product": product})


def cathegory_detail(request, cathegory_id):
    cathegory = Cathegory.objects.get(id=cathegory_id)
    products = cathegory.products.all()
    return render(request, "store/cathegory_detail.html", context={"cathegory": cathegory,"product_list": build_template(products, 3)})


