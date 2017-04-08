from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^village/(?P<village_id>[0-9]+)/json/$', views.village_dump, name='village_dump'),
    url(r'^village/(?P<village_id>[0-9]+)/people/json/$', views.people_dump, name='people_dump'),
    url(r'^village/(?P<village_id>[0-9]+)/groups/json/$', views.groups_dump, name='groups_dump'),
]
