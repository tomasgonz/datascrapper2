''' Download FAO data '''
import re
import requests
from data import Frame
from sources.fao.dataset import Dataset

__version__ = '0.1.0'

__url_datasets__ = "http://fenixservices.fao.org/faostat/static/bulkdownloads/datasets_E.json"

datasets = []

def get_datasets():
    resp = requests.get(url=__url_datasets__)
    ds = resp.json() # Check the JSON Response Content documentation below
    
    for d in ds['Datasets']['Dataset']:
        dset = Dataset()
        dset.DatasetCode = d['DatasetCode']
        dset.DatasetName = d['DatasetName']
        dset.Topic = d['Topic']
        dset.DatasetDescription = d['DatasetDescription']
        dset.Contact = d['Contact']
        dset.Email = d['Email']
        dset.DateUpdate = d['DateUpdate']
        dset.CompressionFormat = d['CompressionFormat']
        dset.FileType = d['FileType']
        dset.FileSize = d['FileSize']
        dset.FileRows = d['FileRows']
        dset.FileLocation = d['FileLocation']
    
        datasets.append(dset)

        return datasets
    
def print_datasets():
    i = 0
    for d in datasets:
        i = i + 1
        print("%s %s" % (i, d.DatasetName))