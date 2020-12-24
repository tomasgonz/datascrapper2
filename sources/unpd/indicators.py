import sys
sys.path.append("../")
import os
import pandas as pd
from data import Frame

cache_folder = os.getcwd().split('datascrapper2')[0] + 'datascrapper2/sources/unpd/data'

def load_projections(dataset = 'all'):
    if dataset == 'all':
        df = pd.read_excel(cache_folder + "/UN_PPP2019_PopTot.xlsx") 

    if dataset == '0-24':
        df = pd.read_excel(cache_folder + "/UN_PPP2019_Output_Pop0-24.xlsx")    

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
    df["0-29"] = df.iloc[:,3:9].sum(axis=1)
    df["0-14"] = df.iloc[:,3:6].sum(axis=1)
    df["0-19"] = df.iloc[:,3:7].sum(axis=1)

    tdf = Frame.Frame()
    cols = df.columns.values
    for i in range(0,len(df)):
        new_row = {}
        for j in range(0, len(df.columns)):
            new_row[cols[j]]=df.iloc[i,j]
        tdf.add_row(new_row)
    return tdf

def get_age_group(age_group, countries):
    data = load_age_groups()
    new_data = Frame.Frame()
    for r in data:
        if (r.get_by_column_name('entity').get_value() in countries):
            new_data.append(r)
            
    new_data = new_data.wide('entity', age_group, 'Reference date (as of 1 July)')

    return new_data

def get_age_group_by_country_groups(age_group, country_groups):
    datasets = []
    for g in country_groups:
        sums = []
        ctrs = geo.countries.get_country_names_and_aliases(geo.countries.get_countries_in_group([g]))
        data = get_age_group(age_group, ctrs)    
        x = data.get_column_names()[1:len(data.get_column_names())]

        for i in range(1,len(data.columns)):
            sums.append(data.columns[i].sum())

        datasets.append([x, sums, g, ''])
        
    return datasets

def get_population_projection(ctrs, dataset='all'):
    new_df = Frame.Frame()
    data_frame = load_projections(dataset=dataset)
    for r in data_frame:
        if (r.get_by_column_name('entity').get_value() in ctrs):
            new_df.rows.append(r)    
    return new_df

def get_projection_by_group(group, dataset='all'):    
    ctrs = c.get_country_names_and_aliases(c.get_countries_in_group([group]))    
    new_df = Frame.Frame()
    data_frame = load_projections(dataset=dataset)
    for r in data_frame:        
        if (r.get_by_column_name('entity').get_value() in ctrs):
            new_df.rows.append(r)    
    
    return new_df

def get_projection_by_groups(groups, dataset='all'):
    datasets = []
    x = get_projection_by_group(groups[0], dataset = dataset).get_column_names()[2:len(get_projection_by_group(groups[0], dataset=dataset).get_column_names())]
    for g in groups:    
        y = get_projection_by_group(g, dataset=dataset).get_total_by_column()[2:len(get_projection_by_group(g, dataset=dataset).get_column_names())]
        datasets.append([x, y, g, 'Projected population, ' + dataset + ', thousands'])
    
    return datasets

