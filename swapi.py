import pandas as pd
import requests

def ppl_api():
    ppl = requests.get('https://swapi.dev/api/people')
    return ppl