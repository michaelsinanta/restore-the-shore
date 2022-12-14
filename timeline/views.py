

from django.shortcuts import render
from create_event.models import Event
from timeline.models import JoinEvent
from django.shortcuts import redirect
from landing_page.models import UserAccount
from django.db.models import F
from timeline.forms import JoinEventForm
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.



def show_data(request):
   

    data_event = Event.objects.all()
    response = {
        'datalist':  data_event,
 
    }  

   
    
    return render(request, "timeline.html", response)


@csrf_exempt
def join_event(request):
    form = JoinEventForm()
    if request.method == "POST":
        form = JoinEventForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return JsonResponse({
                "pk" : form.pk, "fields": {
                "namaEvent" : form.namaEvent,
                "namaPantai" : form.namaPantai,
                "alamatPantai" : form.alamatPantai,
                "jumlahPartisipan" : form.jumlahPartisipan,
                "fotoPantai" : form.fotoPantai,
                "deskripsi" : form.deskripsi,
                "tanggalMulai" : form.tanggalMulai,
                "tanggalAkhir" : form.tanggalAkhir,
            }})

@csrf_exempt
def join_event(request):
    form = JoinEventForm()
    if request.method == "POST":
        form = JoinEventForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return JsonResponse({
                "pk" : form.pk, "fields": {
                "namaEvent" : form.namaEvent,
                "namaPantai" : form.namaPantai,
                "alamatPantai" : form.alamatPantai,
                "jumlahPartisipan" : form.jumlahPartisipan,
                "fotoPantai" : form.fotoPantai,
                "deskripsi" : form.deskripsi,
                "tanggalMulai" : form.tanggalMulai,
                "tanggalAkhir" : form.tanggalAkhir,
            }})

def show_event_by_id(request, pk):
    data = Event.objects.get(id=pk)
    context = {
        'data' : data,
    }
    return render(request, "event_detail.html", context)

def show_json(request):
    data_event = JoinEvent.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")


def show_json_all(request):
    data_event = JoinEvent.objects.all()
    return HttpResponse(serializers.serialize("json", data_event), content_type="application/json")
    
@csrf_exempt
def join_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        print(request.user.username)
        
        namaEvent = data["namaEvent"]
        namaPantai = data["namaPantai"]
        alamatPantai = data["alamatPantai"]
        jumlahPartisipan = data["jumlahPartisipan"]
        fotoPantai = data["fotoPantai"]
        deskripsi = data["deskripsi"]
        tanggalMulai = data["tanggalMulai"]
        tanggalAkhir = data["tanggalAkhir"]
        
        try:
            JoinEvent.objects.get(user=request.user, 

            namaEvent = namaEvent,
            namaPantai = namaPantai,
            alamatPantai = alamatPantai,
            jumlahPartisipan = jumlahPartisipan,
            fotoPantai = fotoPantai,
            deskripsi = deskripsi,
            tanggalMulai = tanggalMulai,
            tanggalAkhir = tanggalAkhir)
            return JsonResponse({"status": "joined"}, status=401)
        except:
            joinEvent = JoinEvent.objects.create(
            user=request.user,
            namaEvent = namaEvent,
            namaPantai = namaPantai,
            alamatPantai = alamatPantai,
            jumlahPartisipan = jumlahPartisipan,
            fotoPantai = fotoPantai,
            deskripsi = deskripsi,
            tanggalMulai = tanggalMulai,
            tanggalAkhir = tanggalAkhir
            )

            joinEvent.save()

        
            return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

    