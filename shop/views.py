from django.shortcuts import render, HttpResponse
from .models import Product, Contact
from math import ceil
from django.contrib import messages
def index(request):
    return render(request,'shop/index.html')

def plants(request):
    products = Product.objects.all()
    print(products)
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        allProds.append([prod,range(1,n),n])
    params = {'allProds' : allProds}
    return render(request,'shop/plants.html', params)

def items(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/items.html', {'product' : product[0]})

def search(request):
    query = request.GET['query']
    if len(query) > 0:
        allProdsname = Product.objects.filter(product_name__icontains=query)
        descpro = Product.objects.filter(desc__icontains=query)
        allProds = allProdsname.union(descpro)
    else:
        allProds = Product.objects.none()
        messages.warning(request, "Please enter something to begin searching.")
    params = {'allProds' : allProds, 'query' : query}
    return render(request,'shop/search.html',params)

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 1 or len(email) < 1 or len(phone) < 1 or len(content) < 1:
            messages.error(request, "Please fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message was delivered successfully. We'll get in touch with you soon.")

    return render(request,'shop/contact.html')


# def productview(request):
#     return render(request,'shop/index.html')
# def checkout(request):
#     return render(request,'shop/index.html')
# def tracker(request):
#     return render(request,'shop/index.html')