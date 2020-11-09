from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("这是一个投票站点")
