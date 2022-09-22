from django.shortcuts import render
from events.models import Event

# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    event_list = Event.objects.order_by('date')
    context = {
        'event_list': event_list,
        'officer_list': (
            ('President', 'First', 'Last'),
            ('Vice President', 'First', 'Last'),
            ('Treasurer', 'First', 'Last'),
            ('Secretary', 'First', 'Last')
        )

    }
    return render(request, 'acmsite/index.html', context)

