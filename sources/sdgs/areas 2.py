import re
import requests
from data.Frame import Frame
from geo.list import CountryList
from sources.sdgs.utils import json_to_frame

areas = Frame()

def load_areas():
    url = 'https://unstats.un.org/SDGAPI/v1/sdg/GeoArea/List'
    areas = json_to_frame(requests.get(url).json())
    return areas
