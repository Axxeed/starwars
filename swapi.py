import pandas as pd
import requests

def import_starships():
    ss = requests.get('https://swapi.dev/api/starships/').json()
    return ss