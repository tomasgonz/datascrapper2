import sys
sys.path.append("../")
import os
import pandas as pd
from data import Frame, Row, Column
from countries.list import CountryList
c = CountryList()
c.load_wb()
cache_folder = os.getcwd().split('datascrapper2')[0] + 'datascrapper2/sources/unpd/data'

def load_projections():
    df = pd.read_excel(cache_folder + "/UN_PPP2019_PopTot.xlsx")
    df = df.rename(columns={'Region, subregion, country or area': 'entity'})
    tdf = Frame.Frame()
    cols = df.columns.values
    for i in range(0,len(df)):
        new_row = {}
        for j in range(0, len(df.columns)):
            new_row[cols[j]]=df.iloc[i,j]
        tdf.add_row(new_row)
    return tdf

def load_age_groups():
    df = pd.read_excel(cache_folder + "/WPP2019_POP_F15_1_ANNUAL_POPULATION_BY_AGE_BOTH_SEXES.xlsx")    
    tdf = Frame.Frame()
    cols = df.columns.values
    for i in range(0,len(df)):
        new_row = {}
        for j in range(0, len(df.columns)):
            new_row[cols[j]]=df.iloc[i,j]
        tdf.add_row(new_row)
    return tdf

def get_population_projection(ctrs):
    new_df = Frame.Frame()
    data_frame = load_projections()
    for r in data_frame:
        if (r.get_by_column_name('entity').get_value() in ctrs):
            new_df.rows.append(r)    
    return new_df

def get_projection_by_group(group):    
    ctrs = c.get_country_names_and_aliases(c.get_countries_in_group([group]))    
    new_df = Frame.Frame()
    data_frame = load_projections()
    for r in data_frame:        
        if (r.get_by_column_name('entity').get_value() in ctrs):
            new_df.rows.append(r)    
    
    return new_df

def get_projection_by_groups(groups):
    datasets = []
    x = get_projection_by_group(groups[0]).get_column_names()[2:len(get_projection_by_group(groups[0]).get_column_names())]
    for g in groups:    
        y = get_projection_by_group(g).get_total_by_column()[2:len(get_projection_by_group(g).get_column_names())]
        datasets.append([x, y, g, 'Projected population, thousands'])
    
    return datasets

