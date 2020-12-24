''' Download SDGs data '''
import re
import requests
from data.Frame import Frame
from sources.sdgs.utils import json_to_frame

__version__ = '0.1.0'
__url__ = "https://unstats.un.org/SDGAPI/v1/"

datasets = []

domains = Frame()
countries = Frame()
indicators = Frame()

def load_indicators():
    url = 'https://unstats.un.org/SDGAPI/v1/sdg/indicator/List'
    indicators = json_to_frame(requests.get(url).json())
    return countries
