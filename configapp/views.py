from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def category(request):
    cat = Categories.objects.all()
    content = {
        "cat":cat,

    }
    return render(request,  'category.html',content)

def product(request):
    product = Products.objects.all()
    content = {
        "product":product
    }
    return render(request, 'products.html',content)

def order_detail(request):
    ordetail = Order_details.objects.all()
    content = {
        "ordetail":ordetail
    }

    return render(request,'order_details.html',content)

def orders(request):
    order = Orders.objects.all()
    content = {
        "order":order
    }

    return render(request,"orders.html",content)

def allfuncmodel(request):
    cat = Categories.objects.all()
    product = Products.objects.all()
    ordetail = Order_details.objects.all()
    order = Orders.objects.all()
    content = {
        "cat":cat,
        "product":product,
        "orderdt":ordetail,
        "order":order,
    }

    return render(request,"allfunc.html",content)