from django.shortcuts import render
from django.http import HttpResponse, Http404

from .graph_exporter import export_graph

def case_dump(request, case_id):
    graph = export_graph(case_id)
    if graph == None:
        raise Http404("Invalid case id")
    return HttpResponse(graph, content_type="application/json")
