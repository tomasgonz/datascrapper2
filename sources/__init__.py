import sources.worldbank
import sources.undp
import sources.unpd
import sources.imf
import sources.comtrade
import sources.fao
import sources.sdgs
import sources.cdp

__all__ = ["worldbank", "undp", "unpd", "imf", "comtrade", "fao", "sdgs", "cdp"]

def get(p):
	if p == 'worldbank':
		return sources.worldbank

def get_properties(p):
	if p == 'worldbank':
		print (sources.worldbank.__all__)
