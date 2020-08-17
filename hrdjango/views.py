from django.shortcuts import render, reverse
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "index.html")
