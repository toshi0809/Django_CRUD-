from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def create(request):
    return render(request, "create.html")


def add(request):
    product = Product(
        title=request.POST["title"],
        description=request.POST["description"],
        price=request.POST["price"],
    )
    product.save()
    return redirect("root")


def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.title = request.POST["title"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.save()
        return redirect("root")
    else:
        return render(request, "edit.html", {"product": product})


def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect("root")
