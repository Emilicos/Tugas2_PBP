from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

def show_mywatchlist_html(request):
    mywatchlist = MyWatchList.objects.all()
    movies_counter = len(MyWatchList.objects.all())
    movies_counter_watched = len(MyWatchList.objects.filter(watched = True))
    if(movies_counter_watched >= movies_counter/2):
        movies_watched = True
    else:
        movies_watched = False
    
    context = {
        "nama": "Alvaro Austin",
        "student_id": 2106752180,
        "mywatchlist": mywatchlist,
        "movies_watched": movies_watched
    }

    return render(request, 'mywatchlist.html', context)

def show_mywatchlist_xml(request):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist), content_type="application/xml")

def show_mywatchlist_json(request):
    mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist), content_type="application/json")
