import sys
import json
import urllib.request
from IPython.display import clear_output
import sources
from geo.list import CountryList
from data.Frame import Frame
from data.Stats import calculate_weighted_average as wa
c = CountryList()
c.load_wb()
from sources.worldbank.indicators import get_data_frame_wide as getdfw
from sources.worldbank.datatable import get_data_table
import bokeh
from bokeh.models import HoverTool, ColumnDataSource,  LabelSet, Label, Legend, LegendItem
from bokeh.plotting import figure, output_file, show, reset_output
import pandas as pd
import numpy as np
from colors import colors

def estimate(years,indicator, groups, weight = None):
    data_df = get_data_table(years, indicator, groups, export_to_excel=False)    
    
    if weight is None:
        return (data_df)    
    
    weight_df = get_data_table(years, weight, groups, export_to_excel=False)
    df_ldcs_w = wa(data_df, weight_df, 'entity' )
    
    return (df_ldcs_w)

def line_chart(series, title, **kwargs):
    # output_file("data.html")
    # create a new plot with a title and axis labels
    
    line_width = 1
    if 'line_width' in kwargs:
        line_width = kwargs['line_width']

    p = figure(title=title, x_axis_label=kwargs['x_axis_label'], 
        y_axis_label=kwargs['y_axis_label'], 
        height = kwargs['height'],
        width = kwargs['width'])        
    j = 0

    #legend_items = []

    #source = ColumnDataSource(data=series) # data for the graph

    for data in series:                
        # output to static HTML file
        # add a line renderer with legend and line thickness
        x = data[0]
        y = data[1]
        group = data[2]
        #legend_items.append(LegendItem(label=data[2], index=j))
        p.line(x, y, line_width=line_width, color = colors[j], legend=data[2])
        p.circle(x, y, color=colors[j], line_width=3)
        j = j + 1
    
    hover = HoverTool()
    hover.tooltips = """                
        <div style=padding=5px>Year:@x</div>
        <div style=padding=5px>Value:@y</div>        
        """
    p.add_tools(hover)
    #legend = Legend(items=legend_items, location="bottom_left")

    #p.add_layout(legend, 'below')    
    p.legend.location = "bottom_left"
    
    #change just some things about the x-grid
    p.xgrid.grid_line_color = None

    # change just some things about the y-grid
    p.ygrid.grid_line_alpha = 0.5

    return p

def scatter_plot(x, y, radii, entities):

    hover = HoverTool(names=entities, tooltips=[('entity', '@entity')])
    
    TOOLS=hover

    source = ColumnDataSource(data=dict(evi=x, hai=y, names=entities, 
                                        radii=radii))

    p = figure(title="HAI vs EVI", 
            x_axis_label='EVI', 
            y_axis_label='HAI', 
            tools=["hover",], height = 600, width = 950)    

    p.scatter(x='evi', y='hai', 
            radius='radii', 
            fill_alpha=0.6, 
            line_color=None,
            source=source)

    labels = LabelSet(x='evi', y='hai', text='names', level='glyph',
                x_offset=5, y_offset=5, source=source,  render_mode='canvas',text_font_size="8pt")
    p.add_layout(labels)

    return p

def show_line_by_line(data, **kwargs):   
    datasets = []
    x = data.get_column_names()[2:len(data.get_column_names())]
    for r in data:
        y = r.as_array()[2: len(r.as_array())]
        group = r.as_array()[0]
        description = "LDCs"
        datasets.append([x,y, group, description])
    
    show(line_chart(datasets, datasets[0][3], 
        x_axis_label=kwargs['x_axis_label'], 
        y_axis_label=kwargs['y_axis_label'], 
        height=kwargs['height'], 
        width=kwargs['width']))
    
    return datasets   

def show_weighted_average(years, indicator, weight, groups):
    datasets = []
    for group in groups:
        data_group = estimate(years, indicator, [[group]], weight)
        x = years
        y = []
        for i in range(3,len(data_group.get_last_row().as_array()), 3):
            y.append(data_group.get_last_row()[i].get_value())
        data_group.entities_description = group
        datasets.append([x,y, group, data_group.description])
    series = datasets
    show(line_chart(series, series[0][3], x_axis_label="Years", y_axis_label=indicator, height=400, width=800))

    return series

def show_group_total(years, indicator, groups):
    datasets = []
    for group in groups:
        data_group = get_data_table(years, indicator, [[group]])
        x = years
        y = []
        for i in range(1,len(data_group.get_total_by_column())):
            y.append(data_group.get_total_by_column()[i])
        data_group.entities_description = group
        datasets.append([x,y, group, data_group.description])
    series = datasets
    show(line_chart(series, series[0][3], x_axis_label="Years", y_axis_label=indicator, height=400, width=900))    

def get_pandas_dataframe(series):
    data = []

    for item in series:
        item[1].insert(0, str(item[2]))
        data.append(item[1])

    series[0][0].insert(0, 'Entity')
    df = pd.DataFrame(data = data, columns = series[0][0])

    return(df)
