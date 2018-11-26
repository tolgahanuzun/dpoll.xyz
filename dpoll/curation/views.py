from django.shortcuts import render


from .models import Blacklist


def index(request):
    blacklist = Blacklist.objects.all()

    return render(request, "blacklist.html", {"blacklist": blacklist})