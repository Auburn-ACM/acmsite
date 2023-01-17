from django.shortcuts import render
from events.models import Event
from random import randint
# Create your views here.

def index(request):
    # return HttpResponse('Hello World!')
    event_list = Event.objects.order_by('date')
    image_num = randint(0, 35)
    context = {
        'event_list': event_list,
        'officer_list': (
            ('President', 'First', 'Last'),
            ('Vice President', 'First', 'Last'),
            ('Treasurer', 'First', 'Last'),
            ('Secretary', 'First', 'Last')
        ),
        'aubie_image': f'acmsite/aubie_photos/aubie_{image_num}.png',
    }
    return render(request, 'acmsite/index.html', context)

def CPT(request):
    context = {
        'title': 'CPT',
        'name': 'Competitive Programming Team',
        'when': 'TBD',
        'where': 'TBD',
        'what': 'TBD',
        'links': {
            # 'website': '/clubs/CPT',
            'discord': 'https://discord.gg/',
            'groupme': 'https://groupme.com/join_group/',
            # 'github': 'https://github.com',
        },
        'officer_list': (
            ('President', 'First', 'Last'),
            # ('Vice President', 'First', 'Last'),
            # ('Treasurer', 'First', 'Last'),
            # ('Secretary', 'First', 'Last')
        )
    }
    return render(request, 'acmsite/clubs_base.html', context)

def EHC(request):
    context = {
        'title': 'EHC',
        'name': 'Ethical Hacking Club',
        'when': 'TBD',
        'where': 'TBD',
        'what': 'TBD',
        'links': {
            'website': 'https://ehc.auburn.edu',
            'discord': 'https://discord.gg/',
            'groupme': 'https://groupme.com/join_group/',
            'github': 'https://github.com',
        },
        'officer_list': (
            ('President', 'First', 'Last'),
            ('Vice President', 'First', 'Last'),
            ('Treasurer', 'First', 'Last'),
            ('Secretary', 'First', 'Last')
        )
    }
    return render(request, 'acmsite/clubs_base.html', context)

def makerspace(request):
    context = {
        'title': 'CS Makerspace',
        'name': 'CS Makerspace',
        'when': 'TBD',
        'where': 'TBD',
        'what': 'TBD',
        'links': {
            # 'website': 'https://ehc.auburn.edu',
            'discord': 'https://discord.gg/',
            'groupme': 'https://groupme.com/join_group/',
            # 'github': 'https://github.com',
        },
        'officer_list': (
            ('President', 'First', 'Last'),
            ('Vice President', 'First', 'Last'),
            ('Treasurer', 'First', 'Last'),
            ('Secretary', 'First', 'Last')
        )
    }
    return render(request, 'acmsite/clubs_base.html', context)

