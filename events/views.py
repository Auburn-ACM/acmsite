from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.

def index(request):
    event_list = Event.objects.order_by('date')
    context = {
        'event_list': event_list,
    }
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/detail.html', context)
