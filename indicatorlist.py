from indicator import *
import json

class IndicatorList(list):

	def search(self, _name):

		results = []

		print(name)

		for ind in List:

			n = ind.name

			if n.find(_name) > -1:
				results.append(ind)

		return results


	def add(self, indicator):

		self.append(indicator)


	def as_json():

		arr = {}

		j = 0
		
		for indicator in self:
			j = j + 1
			arr[str(j)] = indicator.as_json()

		return arr


	def get(_name):

		for i in self:
			if i.name == _name:
				return i

	def save_to_disk():
		with open('indicators.json', 'w') as outfile:
			json.dump(as_json(), outfile)

	def load_from_disk():
		with open('indicators.json', 'r') as f:
			data = json.loads(f)
			
		for i in data:
			print(i)
			ind = Indicator()
			ind.name= i['name']
			ind.description = i['description']
			ind.source = i['source']
			ind.sourcenote = i['sourcenote']
			ind.datasource = i['datasource']
			ind.url=i['url']
			ind.data=i['data']
	
