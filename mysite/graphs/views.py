from django.shortcuts import render
from django.http import HttpResponse, Http404

from .graph_exporter import export_graph, export_people, export_groups

def village_dump(request, village_id):
    graph = export_graph(village_id)
    if graph == None:
        raise Http404("Invalid village id")
    return HttpResponse(graph, content_type="application/json")

def people_dump(request, village_id):
    people = export_people(village_id)
    if people == None:
        raise Http404("Invalid village id")
    return HttpResponse(people, content_type="application/json")

def groups_dump(request, village_id):
    groups = export_groups(village_id)
    if groups == None:
        raise Http404("Invalid village id")
    return HttpResponse(groups, content_type="application/json")
