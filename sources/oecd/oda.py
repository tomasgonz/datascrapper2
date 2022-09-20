import pandas as pd
import os
from geo.groups import *
c = Countries()
c.load_wb()

data = pd.DataFrame()

def load_data():
    global data
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), "table2aoecd.csv"))

# Get's the aggregate of a group of countries, such as LDCs, UMICs, etc.
def get_group_agg(indicators, years, donors, group):
    ctrs = c.get_group(group).get_names()
    
    filtered_data = data[data['Recipient'].isin(ctrs)]
    filtered_data1 = filtered_data[filtered_data['Donor'].isin(donors)]
    filtered_data2 = filtered_data1[filtered_data1['Year'].isin(years)]
    filtered_data3 = filtered_data2[filtered_data2['Aid type'].isin(indicators)]
    
    grouped_data = filtered_data3.groupby('Year', as_index=False).sum()
    grouped_data['Recipient'] = group

    return grouped_data

def get_data(indicators, years, donors, recipients):
    global data
    if data.empty:  
        load_data()
    
    filtered_data = data[data['Recipient'].isin(recipients)]
    filtered_data1 = filtered_data[filtered_data['Donor'].isin(donors)]
    filtered_data2 = filtered_data1[filtered_data1['Year'].isin(years)]
    filtered_data3 = filtered_data2[filtered_data2['Aid type'].isin(indicators)]

    groups = ['LDCs', 'LLDCs' 'SIDS']

    for element in groups:
        if element in recipients:
           filtered_data3 = pd.concat([filtered_data3, 
           get_group_agg(indicators, years, donors, element)])

    return filtered_data3

def get_aid_type():
    global data
    if data.empty:  
        load_data()

    aid_types = data['Aid type'].unique()
    return aid_types

def get_donors():
    global data
    if data.empty:  
        load_data()
    donors = data['Donor'].unique()
    return donors

def get_recipients():
    global data
    if data.empty:  
        load_data()
    recipients = data['Recipient'].unique()
    return recipients

def get_years():
    global data
    if data.empty:  
        load_data()
    years = data['Year'].unique()
    return years