import pandas as pd
import requests


def import_planets():
    pr = requests.get('https://swapi.dev/api/planets/').json()
    return pr


def ppl_api():
    ppl = requests.get('https://swapi.dev/api/people')
    return ppl

def import_species():
    sp = requests.get('https://swapi.dev/api/species/').json()
    return sp



def import_vaisseau():
    r = requests.get("https://swapi.dev/api/starships")
    return r

def vaisseau_json():
    r = requests.get("https://swapi.dev/api/starships")
    jsonr = r.json()

def ppl_json():
    ppljson = ppl.json()
    return ppljson

