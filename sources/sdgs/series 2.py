import re
import requests
from data.Frame import Frame
from countries.list import CountryList
from sources.sdgs.utils import json_to_frame

series = Frame()

def load_series():
    series = json_to_frame(requests.get(url).json())
    return series

def get_series(series_code, area_code, time_period, dimensions, page_size=10000):
    url = 'https://unstats.un.org/SDGAPI/v1/sdg/Series/Data'
    q = "%s?%s&%s&%s&%s&%s" % (url, series_code, area_code, time_period, dimensions, page_size)
    series = json_to_frame(requests.get(url).json())
    return series
