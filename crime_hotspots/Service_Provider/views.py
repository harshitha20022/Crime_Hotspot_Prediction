
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import ClientRegister_Model,review_Model,crime_hotspots_model,recommend_Model,crime_ratio_model,search_ratio_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            crime_ratio_model.objects.all().delete()
            search_ratio_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = crime_hotspots_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=crime_hotspots_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_Crime(request): # Search

   if request.method == "POST":
        kword = request.POST.get('keyword')
        print(kword)
        obj = crime_hotspots_model.objects.all().filter(Q(Crime_Type__contains=kword) | Q(names__contains=kword)| Q(Hotspot_Name__contains=kword))
        obj1 = crime_hotspots_model.objects.all()
        count = obj.count()
        count1 = obj1.count()
        ratio = count / count1
        if ratio != 0:
            search_ratio_model.objects.create(names=kword, ratio=ratio)
        return render(request, 'SProvider/Search_Crime.html', {'objs': obj,'ratio': ratio})
   return render(request, 'SProvider/Search_Crime.html')

def View_All_Crime_Prediction_Details(request): # Search
    ctype=''
    if request.method == "POST":
       ctype = request.POST.get('ctype')

    obj = crime_hotspots_model.objects.all().filter(Crime_Type=ctype)
    obj1 = crime_hotspots_model.objects.all()
    count = obj.count()
    count1 = obj1.count()
    ratio = count / count1

    if ratio!= 0:
        crime_ratio_model.objects.create(names=ctype, ratio=ratio)

    return render(request, 'SProvider/View_All_Crime_Prediction_Details.html', {'objs': obj,'count':ratio})


def View_Crime_By_Area(request): # Positive

     obj = crime_hotspots_model.objects.all()

     return render(request, 'SProvider/View_Crime_By_Area.html', {'objs': obj})

def View_Crime_By_Date(request):

    obj = crime_hotspots_model.objects.all()

    return render(request, 'SProvider/View_Crime_By_Date.html', {'objs':obj})


def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = crime_hotspots_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = crime_hotspots_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = crime_hotspots_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = crime_hotspots_model.objects.values('names').annotate(dcount=Avg('Number_Of_Crimes'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def View_Crime_Details(request):
    obj = crime_hotspots_model.objects.all()
    return render(request, 'SProvider/View_Crime_Details.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts = crime_ratio_model.objects.values('names').annotate(dcount=Avg('ratio'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

def View_Crime_Found_Ratio(request):
    obj = crime_ratio_model.objects.all()
    return render(request, 'SProvider/View_Crime_Found_Ratio.html', {'list_objects': obj})

def View_Search_Ratio(request):
    obj = search_ratio_model.objects.all()
    return render(request, 'SProvider/View_Search_Ratio.html', {'list_objects': obj})







