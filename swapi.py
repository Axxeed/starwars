import pandas as pd
import requests

def import_vaisseau():
    r = requests.get("https://swapi.dev/api/starships")
    return r