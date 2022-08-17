from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from Accounts.models import *


def index(request):
    return render(request, 'index.html', context={})


def about(request):
    return render(request, 'about.html', context={})



