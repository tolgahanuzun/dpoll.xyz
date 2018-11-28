from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from polls.models import User
from .models import Blacklist

members = [ 'emrebeyler', 'isnochys', 'bluerobo', 'tolgahanuzun', 'admin']


def index(request):
    blacklist = Blacklist.objects.filter(expires_at__gte=datetime.now())

    return render(request, "blacklist.html", {"blacklist": blacklist})


def add(request, user, expire_day):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.user.username not in members:
        return HttpResponse('You are not authorized!')

    get_user = User.objects.filter(username=user)
    if not get_user:
        return HttpResponse('User not found.')
    
    if expire_day < 0:
        expire_day = None;
    elif expire_day == 0:
        return HttpResponse('Not funny...')
    else:
        expire_day = datetime.now() + timedelta(days=expire_day)
    try:
        Blacklist.objects.create(user=get_user.first(), expires_at=expire_day)
    except:
        raise Http404

    return HttpResponse('Record created.')
