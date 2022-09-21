from os import stat
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watch_list = MyWatchList.objects.all()

     # menghitung banyak film yang watched
    number_of_watched = 0

    # iterate ke data yang ada
    for data in data_watch_list:
        if data.watched == 'yes':
            number_of_watched += 1
    
    # message yang disampaikan
    if number_of_watched >= 5:
        status = "Selamat, kamu sudah banyak menonton!"
    else:
        status = "Wah, kamu masih sedikit menonton!"

    context = {
        'name': 'Rania Maharani Narendra',
        'student_id': '2106650222',
        'list_of_movies': data_watch_list,
        'status': status,
    }
   
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")