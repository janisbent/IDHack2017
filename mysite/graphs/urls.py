from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cases/(?P<case_id>[0-9]+)/$', views.case_dump, name='case_dump')
]
