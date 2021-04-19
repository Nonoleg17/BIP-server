from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def start_work(request):
    print('23')
    return HttpResponse('ok')
