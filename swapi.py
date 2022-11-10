def vehicles_df():
    vh = pd.DataFrame(import_vehicles()['results'])
    return vh