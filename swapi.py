import pandas as pd
import requests

def import_species():
    sp = requests.get('https://swapi.dev/api/species/').json()
    return sp



def import_vaisseau():
    r = requests.get("https://swapi.dev/api/starships")
    return r

def vaisseau_json():
    r = requests.get("https://swapi.dev/api/starships")
    jsonr = r.json()

def vaisseau_df():
    r = requests.get("https://swapi.dev/api/starships")
    jsonr = r.json()
    df_vaisseau = pd.DataFrame(jsonr)
    return df_vaisseau