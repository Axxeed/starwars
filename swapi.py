import pandas as pd
import requests

def sp_api():
    pr = requests.get("https://swapi.dev/api/people/")
    return pr