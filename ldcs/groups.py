import sys
sys.path.append("..")
import sources
from countries.list import CountryList
from data.Frame import Frame
from data.Row import Row
from data.Cell import Cell
from data.Stats import calculate_weighted_average as wa
c = CountryList()
c.load_wb()

groups=[['LDCs', 'Africa'],['LDCs', 'Asia and the Pacific'],['LDCs', 'America']] 

def get_regionalized_dataframe(data, label_field):	
	# We will store the final result here
	ndf = Frame()
	# Now we get the data that we want to average by region (defined in the groups)
	# and also total
	for g in groups:    
	    # Data points
	    ctrs = c.get_groups(g)
	    for ctry in ctrs:
	    	for r in data.rows:
	    		lv = r.get_by_column_name(label_field).value.get()
	    		if lv == ctry.name or lv in ctry.alias:
	    			r.get_by_column_name(label_field).value.value = ctry.name
	    			ndf.rows.append(r)	    
	return ndf