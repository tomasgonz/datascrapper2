import urllib
import json
from indicator import Indicator
from indicatorlist import IndicatorList
from sources.worldbank.cache import check_cache, load_cache, check_age, cache_folder, get_file_path
from sources.worldbank.cache import retrieve_and_cache

per_page = 30000

Indicators = IndicatorList()

def get(**kwargs):
    # Get data and coordinate cache and retrieval
    p = get_file_path(kwargs['name'])
    if check_cache(p) == False:
        retrieve_and_cache(name=kwargs['name'])
    else:
        check_age(kwargs['name'])
    cached_data = load_cache(p)
    n_data = []
    for item in cached_data['data']:
        if (item['entity'] in kwargs['countries']) and item['date'] in kwargs['years']:
            n_data.append(item)
    
    cached_data['data'] = n_data
    
    return cached_data

def get_data_frame(**kwargs):

    df = Frame.Frame()

    _name = str(kwargs["name"])

    data = get(name=_name, years=kwargs["years"],
        countries=kwargs['countries'])
   
    for item in data['data']:
        df.add_row(item)
    
    df.id = data['name']
    df.description = data['description']
    df.source = data['source']
    df.source_url = data['sourceurl']
    return df

def get_data_frame_wide(**kwargs):

    _name = str(kwargs["name"])

    df = get_data_frame(name=_name,
        years=kwargs["years"],
        countries=kwargs['countries'])

    dfw = df.wide(kwargs['label_field'],
        kwargs['value_field'],
        kwargs['column_field'])

    dfw.name = df.name
    dfw.id = df.id
    dfw.description = df.description
    dfw.source = df.source
    dfw.source_url = df.source_url

    return dfw

def load_all():

    url = 'http://api.worldbank.org/v2/indicators?format=json&per_page=' + \
        str(per_page)

    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    data = json.loads(data)

    for item in data[1]:

        i = Indicator()
        i.name = item['id']
        i.description = item['name']
        i.sourcenote = item['sourceNote']
        i.datasource = item['sourceOrganization']
        i.source = "worldbank"

        Indicators.add(i)
