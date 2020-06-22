from django.shortcuts import render,redirect
from .models import Product,Contact,Order,OrderUpdate
from math import ceil
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse

def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST" :
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,phone=phone,email=email,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def showOrderStatus(request):
    if request.method=="POST" :
        ordID=request.POST.get('ordID','')
        email=request.POST.get('email','')
        order = Order.objects.filter(order_id=ordID, email=email)
        item_list=[]
        qty_list=[]
        final_list=[]
        x=""

        for item in order :
            x=item.itemsJson

        x=x.split(':[')

        for y in range(1,len(x)):
            item=x[y]
            item_list.append(item.split('"')[1])
            qty_list.append(item.split('"')[0][0])

        for y in range(0,len(item_list)) :
            final_list.append([item_list[y],qty_list[y]])


        try :
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=ordID)
                updates = []
                for item in update:
                    updates.append([item.update_desc, item.timestamp])
            else:
                messages.error(request,"No Such Order Found")
                return render(request,'shop/notFound.html')
        except Exception as e:
            messages.error(request, "No Such Order Found")
            return render(request, 'shop/notFound.html')
    return render(request, 'shop/showOrderStatus.html',{'updateList':updates,'items':final_list})

def matchingSearch(item,query) :
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.subcategory.lower() :
        return True
    else :
        return False

def search(request):
    query=request.GET.get('query','')
    query=query.lower()
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    total=0
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        item_by_cat = []
        for item in prod :
            if matchingSearch(item,query)==True :
                item_by_cat.append(item)
        n = len(item_by_cat)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        total=total+n
        allProds.append([item_by_cat, range(1, nSlides), nSlides])
    if total==0 :
        return render(request, 'shop/searchUnsuccessful.html',{'query':query})
    else :
        return render(request, 'shop/searchResult.html',{'allProds':allProds})

def orderplaced(request,ordid):
    return render(request, 'shop/orderPlaced.html',{'ordid':ordid})

def productView(request,myid):
    # Fetch the product using id
    product = Product.objects.filter(id=myid)
    parameters={'product':product[0]}
    return render(request, 'shop/productview.html',parameters)


def checkout(request):
    if request.method=="POST" :
        itemsJson = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email= request.POST.get('email','')
        itemsJson = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        phone = request.POST.get('phone','')
        zipcode = request.POST.get('zipcode','')
        holdername = request.POST.get('holdername', '')
        cardNo = request.POST.get('card4', '')+ request.POST.get('card8', '')+request.POST.get('card12', '')+request.POST.get('card16', '')
        exp = request.POST.get('exp', '')
        cvv = request.POST.get('cvv', '')
        order = Order(itemsJson=itemsJson, name=name, email=email, address=address, city=city,state=state, zipcode=zipcode, phone=phone, cHolder=holdername, cardNo=cardNo, expDate=exp,cvv=cvv,totalPrice=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your order has been placed")
        update.save()
        variable=True
        id=order.order_id
        return render(request, 'shop/checkout.html',{'id':id,'variable':variable})
    return render(request, 'shop/checkout.html')


def HandleSignUp(request) :
    if request.method=='POST' :
        uname = request.POST.get('uname', '')
        fname = request.POST.get('name', '')
        lname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        ipass = request.POST.get('pass', '')
        cpass = request.POST.get('cpass', '')
        if ipass!=cpass :
            messages.success(request, "Password confirmation do not match")
            return render(request, 'shop/notFound.html')
        if len(uname)<8 :
            return HttpResponse("username too short")
        if uname.isalnum()==False :
            return HttpResponse("Usernme should only contain alphabets or numbers")
        user=User.objects.create_user(username=uname,email=email,password=ipass)
        user.first_name = fname
        user.last_name = lname
        user.save()
        return redirect('SiteHome')
    else :
        messages.error(request, "ERROR 404 !! Page Not Found")
        return render(request, 'shop/notFound.html')

def HandleLogin(request) :
    if request.method=='POST' :
        username = request.POST.get('l_name', '')
        pwd = request.POST.get('l_pass', '')

        user=authenticate(username=username,password=pwd)
        if user is not None :
            login(request,user)
            string_passing="Login Succesful ! You are now logged in as "+user.first_name+" "+user.last_name
            messages.success(request,string_passing)
            return redirect('ShopHome')
        else :
            messages.error(request, "Please Enter Correct Credentials!")
            return render(request,'shop/notFound.html')
    else :
        messages.error(request, "ERROR 404 !! Page Not Found")
        return render(request, 'shop/notFound.html')

def HandleLogout(request) :
    if request.method=="POST" :
        logout(request)
        return redirect('SiteHome')

def notFound(request) :
    pass