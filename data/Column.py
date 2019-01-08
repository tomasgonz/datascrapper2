class Column():
	
	def __init__(self):
		self.name=""
		# Collection of all values of the column
		self.cells = []
		pass

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False

	def get_type(self):
		for c in self.cells:
			if c is not None:
				if c.value.value is not None:
					if self.is_number(c.value.value) == False:				
						return "text"
			
		return "number"
					
	def sum(self):
		result = 0
		for c in self.cells:			
			if c.value.value is not None:
				if self.is_number(c.value.value):
					result = float(result) + float(c.value.value)		
		return result

	def get_unique_values(self):
		values = []
		for c in self.cells:
			if (c.get_value() not in values):
				values.append(c.get_value())
		
		return (values)

