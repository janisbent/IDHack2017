import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Person
from .models import Group
from .models import Village
from .models import PersonRelationship
from .models import GroupRelationship

@csrf_exempt
def add_group(request, village_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            new_group = Group(name=data['name'], desc=data['bio'], village=Village.objects.get(pk=village_id))
            new_group.save()
            return HttpResponse()
        except KeyError:
            return HttpResponseBadRequest('Malformed JSON')
    else:
        return HttpResponseBadRequest('Must be POST')

@csrf_exempt
def add_person(request, village_id):
    conv = {'child' : 'CH', 'teen' : 'TE', 'young adult' : 'YA',
            'adult' : 'AD', 'old' : 'OL', 'Male' : 'M',
            'Female' : 'F'}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            if len(data['groups']) > 0:
                g = Group.objects.get(name=data['groups'][0])
            else:
                g = None
            new_person = Person(name=data['name'], age=conv[data['age']],
                                gender=conv[data['gender']], desc=data['bio'],
                                village=Village.objects.get(pk=village_id),
                                group=g)
            new_person.save()
            return HttpResponse()
        except KeyError:
            return HttpResponseBadRequest('Malformed JSON')
    else:
        return HttpResponseBadRequest('Must be POST')

@csrf_exempt
def add_group_relationship(request, village_id):
    conv = {'positive' : 'PS', 'negative' : 'NG', 'neutral' : 'NT'}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            new_relationship = GroupRelationship(g1=Group.objects.get(name=data['party1']), g2=Group.objects.get(name=data['party2']), status=conv[data['quality']], strength=data['strength'], details=data['notes'])
            new_relationship.save()
            return HttpResponse()
        except KeyError:
            return HttpResponseBadRequest('Malformed JSON')
    else:
        return HttpResponseBadRequest('Must be POST')

@csrf_exempt
def add_person_relationship(request, village_id):
    conv = {'positive' : 'PS', 'negative' : 'NG', 'neutral' : 'NT'}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            new_relationship = PersonRelationship(p1=Person.objects.get(name=data['party1']), p2=Person.objects.get(name=data['party2']), status=conv[data['quality']], strength=data['strength'], details=data['notes'])
            new_relationship.save()
            return HttpResponse()
        except KeyError:
            return HttpResponseBadRequest('Malformed JSON')
    else:
        return HttpResponseBadRequest('Must be POST')
