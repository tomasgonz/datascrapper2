from pymongo import MongoClient
import json

conns = {
    "whereistomas.org" : 27017,
    "stats.whereistomas.org" : 27017,
    "localhost" : 27017
    }

def list():
    return conns

def get_conn(connName):

    for c in conns:
        if c.name == connName:
            client = MongoClient(c.getKey(),conns[c.getKey])
            return client

def insert(**kwargs):

    collection = str(kwargs['collection'])

    client = get_conn()
    db = client["stats"]

    name = str(kwargs['name'])
    source = str(kwargs['source'])
    sourceurl = str(kwargs['sourceurl'])
    description = str(kwargs['description'])
    data = kwargs['data']
    start = kwargs['start']
    end = kwargs['end']

    # The true is very important in order to perform upsert
    
    db[collection].update({ "name" : name}, {"$set":{"description" : description, "start" : start, \
    "end" : end, "source" : source, "sourceurl" : sourceurl, "data":data}}, True)
