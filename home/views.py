from django.shortcuts import render, HttpResponse, redirect
from .models import Product,Contact,Category
from django.http import request
from django.core.mail import send_mail
from .forms import ProductForm
from django.core.mail.backends import console
# Create your views here.

def index(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request, 'index.html', context)

def product(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request, 'product.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('description')
        contact=Contact(cn_name=name,cn_email=email,cn_description=message)
        contact.save()
        send_mail(
            f"Message from {name}",
            "message",
            "karthikthunga34@gmail.com",
            ['karthikthunga34@gmail.com'],
            fail_silently=False )
        send_mail(
            f"Hlooo {name}",
            f"Thank You For Reaching Us about {message}\n Please Wait until Our Executive contact You \n Thank You for your Patiance   -Team ECOM",
            "karthikthunga34@gmail.com",
            [email],
            fail_silently=False )
    return render(request, 'contact.html')

def allcat(request):
    categories=Category.objects.all()
    context={'categories': categories}
    return render(request, 'allcat.html', context)

def catprod(request,id):
    category=Category.objects.get(id=id)
    cat_prod=category.product_set.all()
    context={'cat_prod':cat_prod , 'category':category}
    return render(request, 'catprod.html', context)

def createprod(request):
    form = ProductForm()
    if request.method =='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request, 'createprod.html',context)

def updateprod(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method =='POST':
        form=ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'form':form}
    return render(request, 'updateprod.html',context)

def deleteprod(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')