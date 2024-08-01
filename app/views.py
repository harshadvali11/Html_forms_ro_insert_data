from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def htmlforms(request):

    if request.method=='POST':
        return HttpResponse(request.POST['username'])
    return render(request,'htmlforms.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Topic is created')



    return render(request,'insert_topic.html')


def insert_webpage(request):

    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is created')




    return render(request,'insert_webpage.html',d)













