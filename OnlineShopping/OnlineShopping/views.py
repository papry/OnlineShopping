from django.http import  HttpResponse
from django.shortcuts import render
from design.models import Customer
from design.models import Payment
from design.models import Product
from design.models import feedback
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        x1 = request.POST.get("username1")
        x2 = request.POST.get("password1")
        x3 = Customer.objects.filter(Customer_name=x1,Password=x2)
        if x3:
            return render(request,"product.html")
        else:
            return render(request,"login.html")

    else:
        return render(request,"login.html")


def product(request):

    post = Product.objects.filter()
    context = {"post": post}
    return render(request,"product.html",context)



def register(request):
    if request.method=='POST':
        name1 = request.POST.get("name1")
        email1 = request.POST.get("email1")
        password1 = request.POST.get("password1")
        phn = request.POST.get("phn")
        obj = Customer(Customer_name=name1,Email=email1,Password=password1,Phone_no=phn)
        obj.save()
        return render(request,"login.html")
    else:
        return render(request,"register.html")


def order(request):
    if request.method=='POST':
        code = request.POST.get("code")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        total  = request.POST.get("total")
        obj = Payment(product_code=code,quantity=quantity,Price=price,total=total)
        obj.save()
        return render(request,"home.html")
    else:
        return render(request,"order.html")
def feedback(request):
    return render(request,"feedback.html")

