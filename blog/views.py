from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def index(request):
    posts = Blogpost.objects.all()
    return render(request,'blog/index.html',{'posts':posts})

def blogpost(request,ordid):
    post=Blogpost.objects.filter(id=ordid)[0]
    return render(request,'blog/blogpost.html',{'post':post})

def makePost(request):
    return render(request,'blog/makePost.html')

def savePost(request):
    if request.method=="POST" :
        pub=request.POST.get('name','')
        title=request.POST.get('title','')
        head1=request.POST.get('head1','')
        head2=request.POST.get('head2', '')
        head3=request.POST.get('head3', '')
        chead1=request.POST.get('chead1', '')
        chead2=request.POST.get('chead2', '')
        chead3=request.POST.get('chead3', '')
        from datetime import datetime
        z=datetime.today().strftime('%Y-%m-%d')
        blog=Blogpost(publisher=pub,title=title,pub_date=z,head1=head1,head2=head2,chead1=chead1,head3=head3,chead2=chead2,chead3=chead3)
        blog.save()
    return HttpResponse(title)

def search(request):
    query=request.GET.get('query','')
    query=query.lower()
    print(query)
    posts=Blogpost.objects.all()
    final_list=[]
    for item in posts :
        if query in item.title.lower() :
            final_list.append(item)
        elif query in item.head1.lower() :
            final_list.append(item)
        elif query in item.head2.lower():
            final_list.append(item)
        elif query in item.head3.lower():
            final_list.append(item)
        elif query in item.chead1.lower():
            final_list.append(item)
        elif query in item.chead2.lower():
            final_list.append(item)
        elif query in item.chead3.lower():
            final_list.append(item)
        if len(final_list)==0 :
            return render(request, 'blog/blogSearchNotFound.html',{'query':query})
        else :
            return render(request, 'blog/blogSearch.html', {'posts': final_list})
