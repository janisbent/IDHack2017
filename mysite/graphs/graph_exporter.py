import json

from .models import Group
from .models import Case
from .models import Person
from .models import Village
from .models import PersonRelationship
from .models import GroupRelationship

from django.core import serializers
from django.template import loader

import graphs

def export_person(p):
    return {'id' : p.name, 'bio' : p.desc,
            'gender' : p.gender, 'age' : p.age,
            'db_id' : p.id}

def export_group(g):
    return {'id' : g.name, 'desc' : g.desc,
            'db_id' : g.id}

def export_person_links(v, index_mapping):
    links = PersonRelationship.objects.filter(p1__village__id=v.id)
    return [{'source' : index_mapping[r.p1.id],
             'target' : index_mapping[r.p2.id],
             'type' : r.status, 'value' : r.strength} for r in links]

def export_group_links(v, index_mapping):
    links = GroupRelationship.objects.filter(g1__village__id=v.id)
    return [{'source' : index_mapping[r.g1.id],
             'target' : index_mapping[r.g2.id],
             'type' : r.status, 'value' : r.strength} for r in links]

def export_village(v):
    nodes = [export_person(p) for p in v.person_set.all()]
    index_mapping = {}
    for i in range(len(nodes)):
        index_mapping[nodes[i]['db_id']] = i
    obj =  {'name' : v.name, 'desc' : v.desc,
            'nodes' : nodes,
            'links' : export_person_links(v, index_mapping)}
    return obj

def export_village_groups(v):
    nodes = [export_group(g) for g in v.group_set.all()]
    index_mapping = {}
    for i in range(len(nodes)):
        index_mapping[nodes[i]['db_id']] = i
        obj =  {'name' : v.name, 'desc' : v.desc,
                'nodes' : nodes,
                'links' : export_group_links(v, index_mapping)}
    return obj

def export_graph(village_id):
    try:
        v = Village.objects.get(pk=village_id)
    except:
        return None

    return json.dumps(export_village(v), indent=4)

def export_graph_groups(village_id):
    try:
        v = Village.objects.get(pk=village_id)
    except:
        return None

    return json.dumps(export_village_groups(v), indent=4)

# def export_all(village_id):
#     graph = export_graph(village_id)
#     groups = export_graph_groups(village_id)
#     offset = len(graph['nodes'])
#     if graph == None or groups == None:
#         return None

#     graph['nodes'].extend(groups['nodes'])
#     for i in range(len(groups['links'])):
#         groups['links'][i]['source'] += len(

def export_people(village_id):
    try:
        v = Village.objects.get(pk=village_id)
    except:
        return None

    people = []
    for p in v.person_set.all():
        person = {'name' : p.name, 'bio' : p.desc, 'id' : p.id}
        people.append(person)

    return json.dumps(people, indent=4)

def export_groups(village_id):
    try:
        v = Village.objects.get(pk=village_id)
    except:
        return None

    groups = []
    for g in v.group_set.all():
        groups.append({'name' : g.name, 'desc' : g.desc, 'id' : g.id})

    return json.dumps(groups, indent=4)
