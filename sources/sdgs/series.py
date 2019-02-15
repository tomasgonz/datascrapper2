import re
import requests
from data.Frame import Frame
from countries.list import CountryList
from sources.sdgs.utils import json_to_frame

series = Frame()

def load_series():
    url = 'https://unstats.un.org/SDGAPI/v1/sdg/Series/List'
    series = json_to_frame(requests.get(url).json())
    return series

def get_serie():
    pass
