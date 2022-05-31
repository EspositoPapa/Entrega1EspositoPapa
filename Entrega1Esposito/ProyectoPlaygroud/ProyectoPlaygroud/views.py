from django.shortcuts import render
from app_coder.templates import *


def index(request):
    return render(request,'index.html')
