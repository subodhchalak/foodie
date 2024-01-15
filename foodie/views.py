from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    return render(request, "home.html")