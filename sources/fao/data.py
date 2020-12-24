''' Download FAO data '''
import requests
from data.Frame import Frame
from sources.fao.utils import json_to_frame

__version__ = '0.1.0'

__url_datasets__ = "http://fenixservices.fao.org/faostat/static/bulkdownloads/datasets_E.json"

datasets = []

domains = Frame()
countries = Frame()

def get_domains():
    url = 'http://fenixservices.fao.org/faostat/api/v1/en/groupsanddomains'
    domains = json_to_frame(requests.get(url).json())    
    return domains

def load_countries():
    url = 'http://fenixservices.fao.org/faostat/api/v1/en/codes/countries/IG/?show_lists=true'
    countries = json_to_frame(requests.get(url).json())    
    return countries

# Get the code of a country
# needed to perform a query
def get_country_code(c):
    return(countries.search('label', c).rows[0].get_by_column_name('code').get_value())