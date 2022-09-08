import sys
sys.path.append("../..")
sys.path.append("../data")
from sources import *
from data.Frame import Frame
from data.Stats import calculate_weighted_average as wa
from geo.countries import Countries
c = Countries()
import pandas as pd
from pymongo import MongoClient
client = MongoClient('stats.whereistomas.org', username='root', password='Root!0676')
db = client["stats"]
from sources import *

def get_imf_data():    
    imf.weo.retrieve()
    ccodes = pd.read_csv("data/country.csv")
    ccodes.columns = ['iso3code', 'WEO', 'Name']
    data = pd.read_csv("data/values.csv")
    data.columns=['iso3code', 'indicator', 'Date', 'Value']
    data = pd.merge(data, ccodes, on="iso3code", how="left")
    indicators = pd.read_csv("data/indicators.csv")
    indicators.columns = ['indicator', 'title', 'description', 'units', 'scale']
    data = pd.merge(data, indicators, on="indicator", how="left")
    data.columns= ['iso3code', 'indicator', 'Date', 'Value', 'WEO', 'Entity', 'title',
        'description', 'units', 'scale']

    indicators_to_retrieve = [{"indicator": "GGXWDG", "aggregation":True, "weight": "None"},
                            {"indicator": "LUR", "aggregation":True, "weight": "None"},
                            {"indicator": "LP", "aggregation":True, "weight": "None"},
                            {"indicator": "NGDP", "aggregation":True, "weight": "None"},
                            {"indicator": "GGX", "aggregation":True, "weight": "None"},
                            {"indicator": "BCA", "aggregation":True, "weight": "None"},
                            {"indicator": "BCA_NGDPD", "aggregation":True, "weight": "None"},
                            {"indicator": "NGAP_NPGDP", "aggregation":True, "weight": "None"},
                            {"indicator": "NGDPD", "aggregation":True, "weight": "None"},
                            {"indicator": "GGXWDG_NGDP", "aggregation":True, "weight": "None"}]

    inds = []
    for i in indicators_to_retrieve:
        meta = indicators[indicators["indicator"] == i["indicator"]]
        values = []
        ind = data[data['indicator'] == i['indicator']].sort_values(by = 'Date')
        years = ind['Date'].unique().tolist()
        for ii in range(len(ind)):
            date = str(ind.iat[ii, 2])
            value = str(ind.iat[ii, 3])
            value = value.replace(",", "")
            value = float(value) if any([char.isdigit() for char in value]) else None
            entity = str(ind.iat[ii, 5]).lower()
            values.append({'entity':entity, 'date':date, 'value':value})

        indicator = {
            'name' : i["indicator"],
            'aggregation' : False,
            'weight': "None",
            'description': meta.iat[0, 1],
            'years':[],
            'sourcenote': meta.iat[0, 2],
            'connector': "",
            'source':"IMF",
            'sourceurl': "https://www.imf.org/en/Publications/WEO/weo-database/2021/October",
            'keyField': "entity",
            'pivotField': "date",
            'valueField': "value",
            'data' : values
            }
        inds.append(indicator)
        
    for ind in inds:
        db["indicators"].update_one({ "name" : ind['name']}, 
                                    {"$set":{"name" : ind['name'],
                                    "aggregation": ind["aggregation"],
                                    "weight": ind["weight"],
                                    "description" : ind['description'], 
                                    "years" : years, 
                                    "sourceNote" : ind['sourcenote'],
                                    "connector" : ind['connector'],
                                    "source" : ind['source'],
                                    "sourceurl" : ind['sourceurl'], 
                                    "keyField" : "entity",
                                    "pivotField" : "date",
                                    "valueField" : "value",
                                    'data' : ind['data']}}, True)
        print(ind['name'] + " processed.")