import urllib
import json
import os
import os.path
import time
import sources

per_page = 30000
cache_folder = os.getcwd().split('datascrapper2')[0] + 'datascrapper2/sources/worldbank/cache'
# 604800 is on week
max_age = 604800

def get_file_path(name):
    return str(cache_folder) + '/' + str(name) + '.json'
        
def check_age(name):
    if (os.path.getmtime(get_file_path(name)) - time.time()) < -max_age:
        print("Updating " + str(name) + " from server.")
        retrieve_and_cache(name)

def check_cache(name):
    return (os.path.exists(name))

def write_cache(data, file_path):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()
        
def load_cache(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
        return (data)

def retrieve_and_cache(name):
                                                                  
    try:     
        
        url = "http://api.worldbank.org/v2/countries/all/indicators/" + str(name) + "?format=JSON&per_page=" + str(per_page)

        print(url)
        
        response = urllib.request.urlopen(url)
        dd = response.read().decode('utf-8')
        dd = json.loads(dd)

        data = []
        
        if dd[1] != None:
            for item in dd[1]:
                i = {'entity': item['country'][
                    'value'], 'date': item['date'], 'value': item['value']}
                data.append(i)

        indicator = {
            'name': str(dd[1][0]['indicator']['id']).replace(".", ""),
            'description': str(dd[1][0]['indicator']['value']),
            'connector': 'World Bank',
            'sourceurl': 'http://data.worldbank.org/indicator/' + dd[1][0]['indicator']['id'],
            'data': data}

        url = 'http://api.worldbank.org/v2/indicators/SP.POP.TOTL?format=json&per_page=30000'

        response = urllib.request.urlopen(url)
        data = response.read().decode('utf-8')
        data = json.loads(data)

        indicator['sourcenote'] = data[1][0]['sourceNote']
        indicator['source'] = data[1][0]['source']['value']


    except ValueError:
        pass
    
    f = get_file_path(name)
    write_cache(indicator, f)