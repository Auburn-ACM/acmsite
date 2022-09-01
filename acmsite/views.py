from django.shortcuts import render
from events.models import Event

# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    event_list = Event.objects.order_by('date')
    context = {
        'event_list': event_list,
    }
    return render(request, 'acmsite/index.html', context)

