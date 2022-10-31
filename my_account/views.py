from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from landing_page.models import UserAccount
from timeline.models import JoinEvent

# Create your views here.
@login_required(login_url='landing_page:login_user')
def show_account(request):  
    data_user = UserAccount.objects.get(user = request.user)
    for event in JoinEvent.objects.filter(user = request.user):
        data_user.events_joined.add(event)
    context = {
        'user_data' : data_user,
    }
    return render(request, 'my_account.html', context)

def show_json(request):
    data_user = UserAccount.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data_user), content_type="application/json")