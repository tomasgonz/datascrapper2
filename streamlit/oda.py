import sys
sys.path.append("../")
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from sources import oecd
from geo import *
from geo.countries import Countries

c = Countries()
c.load_wb()

ldcs = c.get_group('LDCs').get_names()
odcs = c.get_group('Developing excluding LDCs').get_names()

recipient_groups = ['LDCs', 'LLDCs', 'SIDS', 'Other developing countries']
all_recipient_groups = oecd.oda.get_recipients().tolist() + recipient_groups

# recipient_groups = ['LDCs', 'LLDCs', 'SIDS', 'Other developing countries'] + oecd.oda.get_recipients()

selected_recipient = st.sidebar.multiselect('Recipient groups', all_recipient_groups)

selected_donor = st.sidebar.selectbox('Donors', oecd.oda.get_donors())

selected_aid_type = st.sidebar.selectbox('Aid types', oecd.oda.get_aid_type())

data = oecd.oda.get_data([selected_aid_type], oecd.oda.get_years(), [selected_donor], selected_recipient)

show_data_table = st.sidebar.checkbox("Show data table")

if show_data_table:
    st.dataframe(data)

chart_data = data[['Recipient', 'Year', 'Value']]

if not chart_data.empty:
    line = alt.Chart(chart_data).mark_line().encode( x = 'Year', y='Value', color='Recipient')
    st.altair_chart(line, use_container_width=True)
    chart_data_wide = chart_data[['Recipient', 'Year', 'Value']].pivot_table(index='Recipient', columns='Year', values = 'Value')
    chart_data_wide
    #chart_data.pivot(chart_data, index='Recipient', columns='Year')['Value']

st.write("Destination of Official Development Assistance Disbursements. Geographical breakdown by donor, recipient and for some types of aid (e.g. grant, loan, technical co-operation) on a disbursement basis (i.e. actual expenditures). The data cover flows from all bilateral and multilateral donors except for Tables DAC 1, DAC 4, DAC 5 and DAC 7b which focus on flows from DAC member countries and the EU Institutions.")
st.write("8 April 2022. Next update: June 2022")
st.write("Official Development Assistance (ODA) is defined as those flows to developing countries and multilateral institutions provided by official agencies, including state and local governments, or by their executive agencies, each transaction of which meets the following tests: i) it is administered with the promotion of the economic development and welfare of developing countries as its main objective; and ii) it is concessional in character and conveys a grant element of at least 25 per cent.")