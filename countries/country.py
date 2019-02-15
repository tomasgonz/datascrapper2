class Country:
    name = ''
    aliases = []
    iso2code = ''
    capital = ''
    iso3code = ''
    incomelevel = ''
    capital_longitude = ''
    capital_latitude = ''
    lendingtype = ''
    region = ''
    groups = []
    alias = []
    fao_code = ''
    sdg_code = ''

    def as_json(self):
    	# The replacement of (.) is done to avoid issues with key in mongodb
        return dict(name=self.name.replace(".", ""), aliases=self.aliases, iso2code=self.iso2code, capitalcity=self.capitalcity, iso3code=self.iso3code, incomelevel=self.incomelevel, longitude=self.longitude, latitude=self.latitude, lendingtype=self.lendingtype, region=self.region, groups=self.groups)

    def as_array(self):
        return([self.name, str(self.aliases), self.iso2code, self.capital, self.iso3code, self.incomelevel, self.capital_longitude, self.capital_latitude, self.lendingtype, self.region, str(self.groups), str(self.alias), self.fao_code, self.sdg_code])
