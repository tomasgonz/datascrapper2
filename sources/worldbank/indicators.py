import urllib
import json
from indicator import Indicator
from data import Frame, Row, Column
from indicatorlist import IndicatorList

per_page = 30000

Indicators = IndicatorList()

def get(**kwargs):
    """
    Download data from the worldbank database


    Parameters
    ----------
    name : string
        Name of the indicator to Download
    years : string
        Number of years
    countries: array
        List of countries to filter

    Returns
    -------
    object
        Return an object containing metadata as well as data retrieved

    """
    
    id = str(kwargs["name"])
    date = ''
    iso2 = ''

    # Get countries
    if 'countries' in kwargs:
        ctrs = kwargs["countries"]

        for x in range(len(kwargs["countries"])):

            if x != 0:
                iso2 = iso2 + ";"

            iso2 = iso2 + kwargs["countries"][x].iso2code

    if iso2 != '':
        url = "http://api.worldbank.org/countries/" + \
            iso2 + "/indicators/" + id
    else:
        url = "http://api.worldbank.org/countries/all/indicators/" + id

    url = url + "?format=JSON&per_page=" + str(per_page)

    # Get dates
    years = kwargs['years']
    years.sort()

    date = str(years[0]) + ":" + str(years[len(years)-1])

    if date != '':
        url = url + "&date=" + date

    indicator = None

    try:

        response = urllib.request.urlopen(url)
        dd = response.read().decode('utf-8')
        dd = json.loads(dd)

        data = []

        if dd[1] != None:
            for item in dd[1]:
                i = {'entity': item['country'][
                    'value'], 'date': item['date'], 'value': item['value']}
                data.append(i)

            indicator = {
                'name': str(dd[1][0]['indicator']['id']).replace(".", ""),
                'description': str(dd[1][0]['indicator']['value']),
                'source': 'World Bank',
                'sourceurl': 'http://data.worldbank.org/indicator/' + dd[1][0]['indicator']['id'],
                'years': kwargs['years'],
                'data': data}

    except ValueError:
        pass

    return indicator

def get_data_frame(**kwargs):

    df = Frame.Frame()

    _name = str(kwargs["name"])

    data = get(name=_name, years=kwargs["years"],
        countries=kwargs['countries'])
    data_array = []

    for item in data['data']:
        df.add_row(item)

    return df

def get_data_frame_wide(**kwargs):

    _name = str(kwargs["name"])

    df = get_data_frame(name=_name,
        years=kwargs["years"],
        countries=kwargs['countries'])

    dfw = df.wide(kwargs['label_field'],
        kwargs['value_field'],
        kwargs['column_field'])

    return dfw

def load_all():

    url = 'http://api.worldbank.org/indicators?format=json&per_page=' + \
        str(per_page)

    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    data = json.loads(data)

    for item in data[1]:

        i = Indicator()
        i.name = item['id']
        i.description = item['name']
        i.sourcenote = item['sourceNote']
        i.datasource = item['sourceOrganization']
        i.source = "worldbank"

        Indicators.add(i)
