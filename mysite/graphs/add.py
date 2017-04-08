import json

from django.http import HttpResponse

from .models import Person
from .models import Group

def add_group(request, village):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_group = Group(name=data['name'], desc=data['bio'])
            new_group.save()
        except KeyError:
            return HttpResponseBadRequest('Malformed JSON')
    else:
        return HttpResponseBadRequest('Must be POST')
