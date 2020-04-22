import sys
sys.path.append("../")
import streamlit as st
import numpy as np
import pandas as pd

from sources import worldbank
from geo import *

st.title('Exploration')

ctrs = geo.list.CountryList()
ctrs.load_wb()

ldcs = ctrs.get_country_names_from_groups(['LDCs'])

data = worldbank.indicators.get_data_frame_wide(name='SP.POP.TOTL', 
    years = ['2010','2015','2017'], countries = ldcs,
    label_field = 'entity',
    value_field = 'value',
    column_field='date'
    ).as_pandas()

data