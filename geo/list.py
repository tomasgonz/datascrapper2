import urllib.request
import json
from geo.country import Country
import pickle
#import sources
from texttable import Texttable
import os
from geo.cache import *

from geo.data import ldcs2025, ldcs2018, ldcs2017, lldcs, mics, mics_lower, \
	mics_upper, oecd, sids, africa, asia, \
	america, north_america, central_america, south_america, \
	europe, oecd, pacific_islands, asia_and_the_pacific, \
	developing_excluding_ldcs, \
	country_alias

cache_folder = os.getcwd().split('datascrapper2')[0] + 'datascrapper2/countries/cache'

class CountryList(list):

	def __new__(self):
		if not hasattr(self, 'instance'):
			self.instance = super().__new__(self)
		
		return self.instance

	def __init__(self):
		if len(self) == 0:
			self.load_wb()
		pass

	def __iter__(self):
		self.idx = 0
		return self

	def __next__(self):
		if self.idx < len(self):
			self.idx += 1
			return self[self.idx - 1]
		else:
			raise StopIteration

	# prints the dataframe
	def print(self, **kwargs):

		cols_width = []
		table = Texttable()
		for r in self:
			table.add_row(r.as_array())
		table_s = table.draw()
		return(table_s)

	def __repr__(self):
		self.print()

	def get_country_by_name(self, n):
		for c in self:
			if n == c.name or n in c.alias:
				return c
		return None

	def as_iso2(self, countries):
		iso2_list = []
		for c in countries:
			iso2_list.append(c.iso2code)
		return iso2_list

	def as_iso3(self, countries):
		iso3_list = []
		for country in countries:
			if (self.get_iso3_from_country_name(country) != None):
				iso3_list.append(self.get_iso3_from_country_name(country))
		return iso3_list

	def get_name_from_iso2(self, iso2code):
		for c in self:
			if c.iso2code == iso2code:
				return c.name

	def get_name_from_iso3(self, iso3code):
		for c in self:
			if c.iso3code == iso3code:
				return c.name

	def add_group(self, group,items):
		for c in self:
			if c.name in items:
				c.groups.append(groups)

	def add_country_groupings(self):
		add_group('LDCs', ldcs_all_names)

	def get_country_names(self, ctrs):
		names = []
		for c in ctrs:
			names.append(c.name)
			
		return(names)

	def get_country_names_and_aliases(self, ctrs):
		names = []
		for c in ctrs:
			names.append(c.name)
			for i in c.alias:
				names.append(i)
		return(names)

	# Add group information to country in list
	# based on data stored in lists
	def get_country_groups(self, country):

		groups = []

		if country in ldcs2025:
			groups.append("LDCs2025")

		if country in ldcs2018:
			groups.append("LDCs")

		if country in ldcs2017:
			groups.append("LDCs2017")
		
		if country in lldcs:
			groups.append("LLDCs")

		if country in mics:
			groups.append("MICs")

		if country in mics_lower:
			groups.append("LMICs")

		if country in mics_upper:
			groups.append("UMICs")

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

	# Check if a country belongs to a group
	def is_in_group(self, country):
		for c in self:
			if c.name == country or country in c.groups:
				return True
		return False

	# Check if a country belongs to a region
	def is_in_region(self, country):

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

	def get_country_names_from_groups(self, groups):

		ctrs = self.get_groups(groups)
		country_names = []
		for ctr in ctrs:
			country_names.append(ctr.name)
		
		return country_names

	# Return country names as json
	def as_json(self):
		ctrs = {}
		for w in self:
			ctrs[w.name] = w.as_json()

		return ctrs
	
	# Get group of countries
	def get_countries_in_group(self, g):
		ctrs = []
		for c in self:
			if set(g).issubset(c.groups):
				ctrs.append(c)

		return ctrs
	
	def get_country_names_in_group(self, g):
		ctrs = []
		for c in self:
			if set(g).issubset(c.groups):
				ctrs.append(c.name)

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
		file_name = 'countries'
		p = get_file_path(file_name)
		if check_cache(p) == False:

			retrieve_and_cache(name=file_name)	
		else:
			check_age(file_name)    	
		
		cached_data = load_cache(p)
		
		# Store data in array
		for item in cached_data[1]:
			c = Country()
			c.name = item['name']
			c.iso2code = item['iso2Code']
			c.capitalcity = item['capitalCity']
			c.iso3code = item['id']
			c.incomelevel = item['incomeLevel']['value']
			c.capital_longitude = item['longitude']
			c.capital_latitude = item['latitude']
			c.lendingtype = item['lendingType']['value']
			c.groups = self.get_country_groups(c.name)
			c.region = self.is_in_region(c.name)

			self.append(c)

		# Now we add aliases of countries
		self.load_country_alias()

	def load_fao_code(self):
		sources.fao.data.load_countries()
		for ctr in self:
			f_c = sources.fao.data.countries.search('label', ctr.name).rows[0].get_by_column_name('label').get_value()
			print(f_c)
			ctr.fao_code = f_c

	def load_sdg_code(self):
		areas = sources.sdgs.areas.load_areas()
		for a in areas:
			if (self.get_country_by_name(a.get_by_column_name('geoAreaName').get_value()) is not None):
				self.get_country_by_name(a.get_by_column_name('geoAreaName').get_value()).sdg_code = str(a.get_by_column_name('geoAreaCode').get_value()).split(".")[0]
