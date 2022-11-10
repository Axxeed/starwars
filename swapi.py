import pandas as pd
import requests

def import_species():
    sp = requests.get('https://swapi.dev/api/species/').json()
    return sp

def species_df():
    df = pd.DataFrame(import_species()['results'])
    return df

species = species_df()