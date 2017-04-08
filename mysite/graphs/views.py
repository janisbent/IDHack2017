from django.shortcuts import render
from django.template import loader
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

def data_entry(request, village_id):
    template = loader.get_template("graphs/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def jquery(request):
    f = open('graphs/templates/graphs/jquery-3.2.0.js', 'r')
    response = HttpResponse(content=f, content_type='text/javascript')
    return response


def css(request):
    style = open('graphs/templates/graphs/style.css', 'r')
    response = HttpResponse(content=style, content_type='text/css')
    return response

def js(request):
    f = open('graphs/templates/graphs/form_loading.js', 'r')
    response = HttpResponse(content=f, content_type='text/javascript')
    return response
