import sys
import json
import urllib.request
from IPython.display import clear_output
import sources
from countries.list import CountryList
from data.Frame import Frame
from data.Stats import calculate_weighted_average as wa
c = CountryList()
c.load_wb()
from sources.worldbank.indicators import get_data_frame_wide as getdfw
from sources.worldbank.datatable import get_data_table
import bokeh
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show, reset_output

def estimate(years,indicator, groups, weight = None):
    data_df = get_data_table(years, indicator, groups, export_to_excel=False)    
    
    if weight is None:
        return (data_df)    
    
    weight_df = get_data_table(years, weight, groups, export_to_excel=False)
    df_ldcs_w = wa(data_df, weight_df, 'entity' )
    
    return (df_ldcs_w)


def line_chart(series, title):
    # output_file("data.html")
    # create a new plot with a title and axis labels
    p = figure(title=title, x_axis_label='Years', y_axis_label='Percentage', height = 400, width = 950)    
    colors = ['red', 'blue', 'green', 'orange']
    j = 0
    for data in series:                
        # output to static HTML file
        # add a line renderer with legend and line thickness
        x = data[0]
        y = data[1]
        group = data[2]
        p.line(x, y, legend=group, line_width=2, color = colors[j])
        p.circle(x, y, color=colors[j], fill_color=colors[j], line_width=3)
        j = j + 1
    
    hover = HoverTool()
    hover.tooltips = """
        <div style=padding=5px>Year:@x</div>
        <div style=padding=5px>Value:@y</div>
        """
    p.add_tools(hover)
    p.legend.location = "bottom_left"
    
    return p

def show_weighted_average(years, indicator, weight, groups):
    datasets = []
    for group in groups:
        data_group = estimate(years, indicator, [[group]], weight)
        x = years
        y = []
        for i in range(3,len(data_group.get_last_row().get_array()), 3):
            y.append(data_group.get_last_row()[i].get_value())
        data_group.entities_description = group
        datasets.append([x,y, group, data_group.description])
    series = datasets
    show(line_chart(series, series[0][3]))

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
    show(line_chart(series, series[0][3]))        