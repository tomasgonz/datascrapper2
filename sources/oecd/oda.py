import pandas as pd

data = pd.DataFrame()

def load_data():
    global data
    data = pd.read_csv('table2aoecd.csv')

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
    aid_types = data['Aid type'].unique()
    return aid_types

def get_donors():
    global data
    donors = data['Donor'].unique()
    return donors