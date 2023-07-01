from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.

def firstform(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'firstform.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')

    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        u=request.POST['u']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO, name=na , url=u )[0]
        WO.save()
        return HttpResponse('<h1>Insertion of Webpage is Done</h1>')

    return render(request,'insert_webpage.html')


def insert_accessrecord(request):
    if request.method=='POST':
        na=request.POST['na']
        dt=request.POST['dt']
        au=request.POST['au']

        WO=Webpage.objects.get(name=na)
        AO=Accessrecord.objects.get_or_create(name=WO,date=dt,author=au)[0]
        AO.save()
        return HttpResponse('<h1>Insertion of access is Done</h1>')

    return render(request,'insert_accessrecord.html')