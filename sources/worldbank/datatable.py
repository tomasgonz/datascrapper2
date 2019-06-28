import sources
from data.Frame import Frame
from countries.list import CountryList

c = CountryList()
c.load_wb()

from sources.worldbank.indicators import get_data_frame_wide as getdfw
from sources.worldbank.indicators import get_data_frame as getdf

def get_data_table(years, indicator, groups, export_to_excel=False):
    # We will store the final result here
    ndf = Frame()
    # Now we get the data that we want to average by region (defined in the groups)
    # and also total
    for g in groups:
        # Data points
        df_d = getdf(name=indicator,
            years = years,
            countries=c.get_groups(g)
            )

        df_data = df_d.wide(label_field='entity',
            value_field='value',
            column_field='date')

        for r in df_data.rows:
            ndf.rows.append(r)

    # Produce dataframe that will be returned as a result of the function
    final_df = Frame()
    final_df.add_column(ndf.get_column('entity'))

    for y in years:
        final_df.add_column(ndf.get_column(float('%s.0' % (str(y)))))

    s = ""
    for g in groups:
        for i in g:
            s =  i + "_" + s
    final_df.name = "%s-%s-%s" % (indicator, years, s)

    if export_to_excel == True:
        final_df.to_xlsx()

    return final_df