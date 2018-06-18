import urllib.request
import json
import time

max_rows = '50000'
typ = 'C'

List = []

def load_countries():
    url = 'http://comtrade.un.org/data/cache/reporterAreas.json'

    response = urllib.request.urlopen(url)
    dd = response.read().decode('utf-8')
    dd = json.loads(dd)

    for item in dd['results']:
        List.append({'country' : item['text'], 'id':item["id"]})

    print ("Countries loaded.")

def bec(classcode):
    for country in List:
        download(freq = 'A', typ = 'C',
            px = 'BEC', ps= '2015,2014,2012,2010,2000', r = country['id'],
                p = '0', rg='all', cc=classcode, fmt='json')

def hs(classcode):
    for country in List:
        if country['country'] != 'All':
            time.sleep(40)
            download(freq = 'A', typ = 'C',
                px = 'HS', ps= '2015,2014,2012,2010,2000', r = country['id'], country = country['country'],
                p = '0', rg='all', cc=classcode, fmt='json', folder = '../data/comtrade/hs/' + classcode + "/")

def download(**kwargs):
    url = 'http://comtrade.un.org/api/get?max=' + max_rows + \
        '&type=' + typ + '&freq=' + kwargs['freq'] + '&px=' + kwargs['px'] + \
        '&ps=' +  kwargs['ps'] + '&r=' + kwargs['r'] + '&p=' + kwargs['p'] + '&rg=' + kwargs['rg'] + \
        '&cc=' + kwargs['cc'] + '&fmt=' + kwargs['fmt']

    response = urllib.request.urlopen(url)
    dd = response.read().decode('utf-8')
    dd = json.loads(dd)

    with open(kwargs['folder'] + kwargs['px'] +
        "." + kwargs['country'] + ".json", "w") as outfile:
        json.dump(dd, outfile)
        outfile.close()

# load_countries()
