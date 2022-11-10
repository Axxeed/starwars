def import_species():
    sp = requests.get('https://swapi.dev/api/species/').json()
    return sp