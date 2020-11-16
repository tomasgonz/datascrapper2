import sys
sys.path.append("../")
import streamlit as st
import numpy as np
import pandas as pd

from sources import worldbank
from geo import *

import plotly.express as px
import plotly.graph_objects as go

st.title('LDCs at a glance')

st.header("GDP")

ldcs = geo.groups.get_group("LDCs").get_names()

years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007','2008', '2009', '2010','2015','2017']

data = worldbank.indicators.get_data_frame(name='EG.ELC.ACCS.ZS', 
    years = years, 
    countries = ldcs    
    ).as_pandas()

data_wide = worldbank.indicators.get_data_frame_wide(name='SP.POP.TOTL', 
    years = years, 
    countries = ldcs,
    label_field = 'entity',
    value_field = 'value',
    column_field='date'
    ).as_pandas()

data_wide

countries = data["entity"].unique().tolist()
countries.insert(0, "All")

indicators = ["GDP", "Access to electricity"]

select_country = st.sidebar.selectbox("Countries", countries)

select_indicator = st.sidebar.selectbox("Indicators", indicators)

filtered_data = []

if select_country == "All":
    filtered_data = data
else:
    filtered_data = data[data["entity"] == select_country]

fig = px.line(filtered_data, 
    title = "Data for " + select_country,
    line_group = "entity", 
    x = "date", 
    y = "value", 
    hover_name="entity", 
    color="entity")
fig.update_layout(showlegend=False, height=800)


st.plotly_chart(fig)


