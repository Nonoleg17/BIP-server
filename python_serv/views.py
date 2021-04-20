from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalData


# Create your views here.
def start_work(request):
    t = PersonalData.objects.create(uid='213', name='123', surname='123',group='123')
    t.save()
    return HttpResponse('ok')
