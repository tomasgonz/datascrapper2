import urllib
import json
import json
import os.path
import time

per_page = 30000
        
def check_age(file_path):
    return(os.path.getmtime(file_path) - time.time())

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

def retrieve_and_cache(**kwargs):
    url = "http://api.worldbank.org/countries/all/indicators/" + str(kwargs['name']) + "?format=JSON&per_page=" + str(per_page)
                                                                     
    try:

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
            'source': 'World Bank',
            'sourceurl': 'http://data.worldbank.org/indicator/' + dd[1][0]['indicator']['id'],
            'data': data}
            
    except ValueError:
        pass
    f = 'data/' + kwargs['name'] + ".json"
    write_cache(indicator, f)