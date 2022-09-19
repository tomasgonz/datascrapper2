import pandas as pd
import os

data = pd.DataFrame()

def load_data():
    global data
    data = pd.read_csv(os.path.join(os.path.dirname(__file__), "table2aoecd.csv"))

def get_data(indicators, years, donors, recipients):
    global data
    if data.empty:  
        load_data()
    
    filtered_data = data[data['Recipient'].isin(recipients)]
    filtered_data1 = filtered_data[filtered_data['Donor'].isin(donors)]
    filtered_data2 = filtered_data1[filtered_data1['Year'].isin(years)]
    filtered_data3 = filtered_data2[filtered_data2['Aid type'].isin(indicators)]

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

def get_years():
    global data
    if data.empty:  
        load_data()
    years = data['Year'].unique()
    return years