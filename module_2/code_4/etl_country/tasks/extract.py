import requests
import json

'''
link to restcountries
https://restcountries.com/
https://restcountries.com/v3.1/region/America
'''

def extract():
    """
    extract data from restcountries
    """
    URL = "https://restcountries.com/v3.1/region/America"
    response = requests.get(URL)
    
    extract_data = []
    if response.status_code == 200:
        
        extract_data = response.json()
        print("Extracted Data ...")
        
        # Save file
        ''' 
        with open('countries_of_america.json', 'w', encoding='utf-8') as f:
            json.dump(extract_data, f, indent=4, ensure_ascii=False)
        '''
                
    return extract_data