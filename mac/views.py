from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.

def index(request):
    URL = 'https://timesofindia.indiatimes.com/news'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    List = []
    for links in soup.find_all('span', {'class': 'w_tle'}):
        List.append(links.text)
    return render(request,'index.html',{'list':List})

def news(request):
    from bs4 import BeautifulSoup
    import requests
    URL = 'https://timesofindia.indiatimes.com'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    List = []
    for data in soup.find_all('ul', {'class': 'list9'}):
        for li in data.find_all('li'):
            List.append([li.a.text, "https://timesofindia.indiatimes.com" + li.a.get('href')])

    return render(request,'newshome.html',{'list':List})

def newspost(request):
    from bs4 import BeautifulSoup
    import requests
    URL=request.GET.get('query','')
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    title=''
    brief=''
    for data in soup.find_all('h1', {'class': 'K55Ut'}):
        title = data.text
    for data in soup.find_all('div', {'class': '_1IaAp clearfix'}):
        for div in data.find_all('div', {'class': '_3WlLe clearfix'}):
            brief = div.text
    if title=='' :
        return HttpResponse('Error!! this particular page could not be opened as this site is currently under development<br>Kindly try another page')
    return render(request,'newspost.html',{'title':title,'text':brief})
