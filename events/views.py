from django.shortcuts import render, get_object_or_404
from .models import Event

# Create your views here.

def index(request):
    event_list = Event.objects.order_by('date')
    context = {
        'event_list': event_list,
    }
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/detail.html', context)
