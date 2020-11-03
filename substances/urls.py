""" urls for the substances app """
from django.urls import path, re_path
from substances import views


urlpatterns = [
    path("", views.home, name='home'),
    path("list", views.sublist, name='list'),
    re_path(r'^search/(?:(?P<query>.+)/)?$', views.search, name='search'),
    path("view/<subid>", views.subview, name='subview'),
    path("view/<subid>/subids", views.subids, name='subids'),
    path("view/<subid>/subdescs", views.subdescs, name='subdescs'),
    path("ingest/<identifier>", views.add, name='add'),
    path("ingest/", views.ingest, name='ingest'),
    path("ingestlist/", views.ingestlist, name='ingestlist'),
    path("normalize/<identifier>", views.normalize, name='normalize'),
]
