import json

from .models import Group
from .models import Case
from .models import Person
from .models import Village
from .models import PersonRelationship
from .models import GroupRelationship

from django.core import serializers

import graphs

def export_person(p):
    return {'id' : p.name, 'bio' : p.desc,
            'gender' : p.gender, 'age' : p.age,
            'db_id' : p.id}

def export_person_links(v, index_mapping):
    links = PersonRelationship.objects.filter(p1__village__id=v.id)
    return [{'source' : index_mapping[r.p1.id],
             'target' : index_mapping[r.p2.id],
             'type' : r.status, 'value' : r.strength} for r in links]

def export_village(v):
    nodes = [export_person(p) for p in v.person_set.all()]
    index_mapping = {}
    for i in range(len(nodes)):
        index_mapping[nodes[i]['db_id']] = i
    node_obj =  {'name' : v.name, 'desc' : v.desc,
                 'person_graph': {'nodes' : nodes,
                                  'links' : export_person_links(v, index_mapping)}}
    return node_obj

def export_graph(case_id):
    try:
        case = Case.objects.get(pk=case_id)
    except:
        return None


    return json.dumps([export_village(v) for v in case.villages.all()], indent=4)
