import sys
sys.path.append("../")
import streamlit as st
import pandas as pd

from sources import oecd
from geo import *
from geo.countries import Countries

c = Countries()
c.load_wb()

ldcs = c.get_group('LDCs').get_names()
odcs = c.get_group('Developing excluding LDCs').get_names()

recipient_groups = ['LDCs', 'LLDCs', 'SIDS', 'Other developing countries']

selected_recipients = st.sidebar.multiselect('Recipient groups', ldcs)

selected_donors = st.sidebar.multiselect('Donors', oecd.oda.get_donors())

selected_aid_types = st.sidebar.multiselect('Aid types', oecd.oda.get_aid_type())

selected_years = st.sidebar.multiselect('Years', oecd.oda.get_years())

data = oecd.oda.get_data(selected_aid_types, selected_years, selected_donors, selected_recipients)

show_data_table = st.sidebar.checkbox("Show data table")

if show_data_table:
    data

chart_data = data[['Recipient', 'Year', 'Value']]

st.line_chart(chart_data, x ='Recipient', y='Value')



