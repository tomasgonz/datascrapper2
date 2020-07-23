import sys
sys.path.append("../..")
import sources
from geo.countries import Countries
c = Countries()
c.
import urllib
import requests
import os
import os.path
import time
import json

cache_folder = '..'
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
    url = 'https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/factbook.json'
    r = requests.get(url)
    f = get_file_path(name)
    write_cache(r.json(), f)

def get_CIA_factbook(**kwargs):
    p = get_file_path(kwargs['name'])
    if check_cache(p) == False:
        retrieve_and_cache(name=kwargs['name'])
    else:
        check_age(kwargs['name'])
    cached_data = load_cache(p)
    
    return cached_data