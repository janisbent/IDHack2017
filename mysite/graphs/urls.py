from django.conf.urls import url

from . import views
from . import add

urlpatterns = [
    url(r'^village/(?P<village_id>[0-9]+)/json/$', views.village_dump, name='village_dump'),
    url(r'^village/(?P<village_id>[0-9]+)/people/json/$', views.people_dump, name='people_dump'),
    url(r'^village/(?P<village_id>[0-9]+)/groups/json/$', views.groups_dump, name='groups_dump'),
    url(r'^village/(?P<village_id>[0-9]+)/add_group/$', add.add_group, name='add_group'),
    url(r'^village/(?P<village_id>[0-9]+)/$', views.data_entry, name='data_entry'),
    url(r'^village/(?P<village_id>[0-9]+)/add_person/$', add.add_person, name='add_person'),
    url(r'^village/(?P<village_id>[0-9]+)/add_rel/$', add.add_group_relationship, name='add_group_relationship'),
]
