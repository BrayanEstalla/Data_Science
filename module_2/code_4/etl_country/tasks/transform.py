from datetime import datetime

def transform(data):
    """
    transform data from restcountries
    """
    transform_data = []
    for countries in data:
        country = countries['name']['common']
        capital = countries['capital'][0] if 'capital' in countries and countries['capital'] else "N/A"
        population = countries['population']
        region = countries['region']
        transform_data.append([country, capital, population, region])
    print("Transformed Data ...")
      
    return transform_data