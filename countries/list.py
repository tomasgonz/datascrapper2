import urllib.request
import json
from countries.country import Country
import pickle

from countries.data import ldcs2018, ldcs2017, mics, mics_lower, \
	mics_upper, oecd, sids, africa, asia, \
	america, north_america, central_america, south_america, \
	europe, oecd, pacific_islands, asia_and_the_pacific, \
	developing_excluding_ldcs, \
	country_alias

class CountryList(list):

	def get_country_by_name(self, n):
		
		for c in self:
			if n == c.name or n in c.alias:
				return c
		
		return None

	def get_countries_as_iso2_list(self, countries):
		iso2_list = []
		for country in countries:
			if (self.get_iso2_from_country_name(country) != None):
				iso2_list.append(self.get_iso2_from_country_name(country))
		return iso2_list

	def get_countries_as_iso3_list(self, countries):
		iso3_list = []
		for country in countries:
			if (self.get_iso3_from_country_name(country) != None):
				iso3_list.append(self.get_iso3_from_country_name(country))
		return iso3_list

	def get_iso2_from_country_name(self, country):
		for c in self:
			if c.name == country:
				return c.iso2code

	def get_iso3_from_country_name(self, country):
		for c in self:
			if c.name == country:
				return c.iso3code

	def get_country_from_iso2(self, iso2code):
		for c in self:
			if c.iso2code == iso2code:
				return c.name

	def get_country_from_iso3(self, iso3code):
		for c in self:
			if c.iso3code == iso3code:
				return c.name

	def add_group(self, group,items):
		for c in self:
			if c.name in items:
				c.groups.append(groups)

	def add_country_groupings(self):
		add_group('LDCs', ldcs_all_names)

	# Add group information to country in list
	# based on data stored in lists
	def checkgroup(self, country):

		groups = []

		if country in ldcs2018:
			groups.append("LDCs")

		if country in ldcs2017:
			groups.append("LDCs2017")

		if country in mics:
			groups.append("MICs")

		if country in mics_lower:
			groups.append("MICs Lower")

		if country in mics_upper:
			groups.append("MICs Upper")

		if country in oecd:
			groups.append("OECD")

		if country in sids:
			groups.append("SIDS")

		if country in pacific_islands:
			groups.append("Pacific islands")

		if country in asia_and_the_pacific:
			groups.append("Asia and the Pacific")

		if country in africa:
			groups.append("Africa")

		if country in asia:
			groups.append("Asia")

		if country in america:
			groups.append("America")

		if country in oecd:
			groups.append("OECD")

		if country in developing_excluding_ldcs:
			groups.append("Developing excluding LDCs")

		return groups

	# Check if a country belongs to a region
	def checkregion(self, country):

		if country in africa:
			return "Africa"

		if country in asia:
			return "Asia"

		if country in north_america:
			return "North America"

		if country in central_america:
			return "Central America"

		if country in south_america:
			return "South America"

		if country in europe:
			return "Europe"


	# Return name of countries as a list
	def get_List(self, cs):

		ctrs = []

		for c in cs:
			for w in self:
				if c == w.name:
					ctrs.append(w)

		return ctrs



	def get_List_as_json(self, cs):
		ctrs = {}

		for c in cs:
			for w in self:
				if c == w.name:
					ctrs[w.name] = w.as_json()

		return ctrs

	# Return country names as json
	def as_json(self):
		ctrs = {}

		for w in self:
			ctrs[w.name] = w.as_json()

		return ctrs

	# Get group of countries
	def get_groups(self, g):
		ctrs = []
		for c in self:          			
			if set(g).issubset(c.groups):
				ctrs.append(c)

		return ctrs


	# Get single group names as stored in countries
	def get_group_names(self, g):
		ctrs = []
		for c in self:
			if g in c.groups:
				ctrs.append(c.name)     
		return ctrs

	def set_country_alias(self, c, a):
		for ctry in self:				
			if ctry.name == c:
				ctry.alias = a

	def load_country_alias(self):
		for k in country_alias:			
			self.set_country_alias(k,country_alias[k])	

	def load_wb(self):
		# Load country data from the worldbank
		# We fetch data from the World Bank
		url = "http://api.worldbank.org/countries?format=json&per_page=30000"
		response = urllib.request.urlopen(url)
		codec = response.info().get_param('charset', 'utf8')
		data = json.loads(response.read().decode(codec))

		# Store data in array
		for item in data[1]:
			c = Country()
			c.name = item['name']
			c.iso2code = item['iso2Code']
			c.capitalcity = item['capitalCity']
			c.iso3code = item['id']
			c.incomelevel = item['incomeLevel']['value']
			c.capital_longitude = item['longitude']
			c.capital_latitude = item['latitude']
			c.lendingtype = item['lendingType']['value']
			c.groups = self.checkgroup(c.name)
			c.region = self.checkregion(c.name)

			self.append(c)

		# Now we add aliases of countries
		self.load_country_alias()

		# Save to disk
		pkl = open("countries.pkl", "wb")
		pickle.dump(c, pkl)