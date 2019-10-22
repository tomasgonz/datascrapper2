import sys
sys.path.append("../")
import pandas as pd
from data import Frame, Row, Column
def get_population_proyections():
    df = pd.read_excel('../data/UN_PPP2019_PopTot.xlsx')
    tdf = Frame.Frame()
    cols = df.columns.values
    for i in range(0,len(df)):
        new_row = {}
        for j in range(0, len(df.columns)):
            new_row[cols[j]]=df.iloc[i,j]
        tdf.add_row(new_row)

    return tdf