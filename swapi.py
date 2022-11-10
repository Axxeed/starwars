
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
    return jsonr

def ppl_json():
    ppljson = ppl.json()
    return ppljson

def vaisseau_df():
    r = requests.get("https://swapi.dev/api/starships")
    jsonr = r.json()
    df_vaisseau = pd.DataFrame(jsonr["results"])
    return df_vaisseau

def import_film():
    r = requests.get("https://swapi.dev/api/films")
    return r

def film_json():
    r = requests.get("https://swapi.dev/api/films")
    jsonr = r.json()
    
def film_df():
    r = requests.get("https://swapi.dev/api/films")
    jsonr = r.json()
    df_film = pd.DataFrame(jsonr["results"])
    return df_film