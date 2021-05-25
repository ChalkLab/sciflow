""" functions file for the datafiles app"""
from crosswalks.models import *


def getnspaces():
    """get a list of namespaces"""
    # spaces = Nspaces.objects.all().values_list()
    spaces = Nspaces.objects.all()
    return spaces


def getnspace(nsid):
    """get the data about a namespace"""
    space = Nspaces.objects.get(id=nsid)
    return space


def onttermsbyns(nsid):
    """get the ont terms using a namespace"""
    terms = Ontterms.objects.all().filter(nspace_id=nsid)
    return terms


def getterm(tid):
    """get the data for an ont term"""
    term = Ontterms.objects.get(id=tid)
    return term