from django.shortcuts import render

# Create your views here.


def supplierAddProduct(request):
    return render(request,'supplier/addproduct.html')

def supplierViewProduct(request):
    return render(request,'supplier/view_product.html')

def supplierOrders(request):
    return render(request,'supplier/orders.html')

def supplierPass(request):
    return render(request,'supplier/pass.html')

def supplierProfile(request):
    return render(request,'supplier/view_product.html')
