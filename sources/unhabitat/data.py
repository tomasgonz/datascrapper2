import re
import requests
from data.Frame import Frame
from countries.list import CountryList

__url_datasets = 'http://urbandata.unhabitat.org/wp-admin/admin-ajax.php?action=load_from_oipa&call=indicator-filter-options&format=json'

regions = Frame()
indicators = Frame()
cities = Frame()
countries = Frame()

def load_datasets():
    url = __url_datasets
    
    domains = json_to_frame(requests.get(url).json())    
    return domains

