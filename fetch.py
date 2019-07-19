import urllib

try:
    import json
except ImportError:
    import simplejson as json

def _fetch(url):
	    '''Downloads data from a JSON page and parses into python objects
	    
	    This method will work for any JSON encoded page, not just World Bank's data.
	    '''
	    
	    f = urllib.urlopen(url)
	    response = json.loads(f.read())
	    f.close()
	    return response

class fetcher(object):
    
    URL = ''

	

	