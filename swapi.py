import pandas as pd
import requests

def import_planets():
    pr = requests.get('https://swapi.dev/api/planets/').json()
    return pr