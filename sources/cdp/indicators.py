import sys
sys.path.append("../")
import pandas as pd
from data import Frame, Row, Column
from countries.list import CountryList
c = CountryList()
c.load_wb()
un_ldc_data_2018_data_source = '../../sources/cdp/data/ldc_data_2018.xlsx'

def load_data():
    df = pd.read_excel(un_ldc_data_2018_data_source)    
    tdf = Frame.Frame()
    cols = df.columns.values
    for i in range(0,len(df)):
        new_row = {}
        for j in range(0, len(df.columns)):
            new_row[cols[j]]=df.iloc[i,j]
        tdf.add_row(new_row)
    return tdf

def get_indicators(groups = []):
    data = load_data()
    new_df = Frame.Frame()
    ctrs = []
    if len(groups) > 0:
        for g in groups:
            ctrs = ctrs + c.get_country_names_and_aliases(c.get_countries_in_group([g]))    
        
        for r in data:
            if (r.get_by_column_name('entity').get_value() in ctrs):
                new_df.rows.append(r)    
        return new_df

    return(load_data())


