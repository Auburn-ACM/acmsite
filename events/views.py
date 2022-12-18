from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Event

# Create your views here.

def index(request):
    event_list = Event.objects.order_by('date')
    curr_date = datetime.now().date()
    upcoming_event_list = []
    past_event_list = []
    for event in event_list:
        if event.date >= curr_date:
            upcoming_event_list.append(event)
        else:
            past_event_list.append(event)
    
    context = {
        'upcoming_event_list': upcoming_event_list,
        'past_event_list': past_event_list,
    }
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {
        'event': event,
    }
    return render(request, 'events/detail.html', context)
