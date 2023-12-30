import random

from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages
# Create your views here.

def homepage(request):
    return render(request,"homepage.html",{})

def addProduct(request):
    if request.method == "GET":
        return render(request,'addProduct.html',{})
    else:
        try:
            Name = request.POST['Name']
            price = request.POST['price']
            discount_price = request.POST['discount_price']
            Brand = request.POST['Brand']
            slug = '_'.join(Name)[:100]+str(random.randint(1,1000))
            description = request.POST['description']
            color = request.POST['color']
            SellerName = request.POST['SellerName']
            Stock = request.POST['Stock']
            newProduct = Product.objects.create(
                Name=Name,
                price=price,
                discount_price=discount_price,
                Brand=Brand,
                slug=slug,
                description=description,
                SellerName=SellerName,
                Stock=Stock,
                color=color
            )
            if request.FILES.get('image1'):
                newProduct.image1 = request.FILES['image1']
            if request.FILES.get('image2'):
                newProduct.image2 = request.FILES['image2']
            if request.FILES.get('image3'):
                newProduct.image3 = request.FILES['image3']
            if request.FILES.get('image4'):
                newProduct.image4 = request.FILES['image4']
            if request.POST.get('video'):
                newProduct.video = request.POST['video']
            newProduct.save()
        except Exception as e:
            messages.error(request,f"Unable to process your request due to the error --> {e}")
            return redirect('inventory_management:addProduct')
        else:
            messages.success(request,"Product added to inventory")
            return redirect('inventory_management:homepage')


def getAllProducts(request):
    allProducts = Product.objects.all()
    c = 0
    refined = []
    temp = []
    for p in allProducts:
        temp.append(p)
        c+=1
        if c==4:
            refined.append(temp)
            c=0
            temp = []
    if c!=0:
        refined.append(temp)
    return render(request,"getAllProducts.html",{'products':refined})