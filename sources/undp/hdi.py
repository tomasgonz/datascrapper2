import json
import urllib

from indicator import Indicator

# Address that stores HDI trends data
url_hdi_trends = "https://data.undp.org/resource/y8j2-3vi9.json"

def get():

    hdi = json.load(urllib.urlopen(url_hdi_trends))
    data = []
    for i in range(0, len(hdi)):
        if '_1980_hdi_value' in hdi[i]:
            a = {'entity': hdi[i]['country'], 'value': hdi[i]['_1980_hdi_value'], 'date': "1980"}
            data.append(a)

        if '_1980_hdi_value' in hdi[i]:
            b = {'entity': hdi[i]['country'], 'value': hdi[i]['_1990_hdi_value'], 'date': "1990"}
            data.append(b)

        if '_2000_hdi_value' in hdi[i]:
            c = {'entity': hdi[i]['country'], 'value': hdi[i]['_2000_hdi_value'], 'date': "2000"}
            data.append(c)

        if '_2005_hdi_value' in hdi[i]:
            d = {'entity': hdi[i]['country'], 'value': hdi[i]['_2005_hdi_value'], 'date': "2005"}
            data.append(d)

        if '_2008_hdi_value' in hdi[i]:
            e = {'entity': hdi[i]['country'], 'value': hdi[i]['_2008_hdi_value'], 'date': "2008"}
            data.append(e)

        if '_2010_hdi_value' in hdi[i]:
            f = {'entity': hdi[i]['country'], 'value': hdi[i]['_2010_hdi_value'], 'date': "2010"}
            data.append(f)

        if '_2011_hdi_value' in hdi[i]:
            g = {'entity': hdi[i]['country'], 'value': hdi[i]['_2011_hdi_value'], 'date': "2011"}
            data.append(g)

        if '_2012_hdi_value' in hdi[i]:
            h = {'entity': hdi[i]['country'], 'value': hdi[i]['_2012_hdi_value'], 'date': "2012"}
            data.append(h)

        if '_2013_hdi_value' in hdi[i]:
            j = {'entity': hdi[i]['country'], 'value': hdi[i]['_2013_hdi_value'], 'date': "2013"}
            data.append(j)

        return data
