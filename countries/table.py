from countries.list import CountryList
from data.Frame import Frame

def get(data, groups, country_field):    
    # We will store the final result here
    ndf = Frame()

    cl = CountryList()
    cl.load_wb()
    
    # Now we get the data that we want to average by region (defined in the groups)
    # and also total
    # Let's conflate 
    cs = []
    
    for cnt in cl.get_groups(groups):
        if cnt.name not in cs:
            cs.append(cnt.name)

    for r in data.rows:
        if r.get_by_column_name(country_field).value.get() in cs:            
            ndf.rows.append(r)
    
    return ndf