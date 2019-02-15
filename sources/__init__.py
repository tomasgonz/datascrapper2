import sources.worldbank
import sources.undp
import sources.imf
import sources.comtrade
import sources.fao
import sources.sdgs

__all__ = ["worldbank", "undp", "imf", "comtrade", "sdgs"]

def get(p):
	if p == 'worldbank':
		return sources.worldbank

def get_properties(p):
	if p == 'worldbank':
		print (sources.worldbank.__all__)
