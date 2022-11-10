import pandas as pd
import requests

def import_planets():
    pr = requests.get('https://swapi.dev/api/planets/').json()
    return pr

def planets_df():
    tr = pd.DataFrame(import_planets["results"])
    return tr
    

