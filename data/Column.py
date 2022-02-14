# Creating a new class called Column that is inheriting from the built-in type list.
class Column(list):

	def __init__(self):
		self.name = ""
		# Collection of all values of the column
		pass

	def add(self, values):
		'''
		Add the values in the list to the values in the cells
		
		:param values: The values to add to the cells
		:return: Nothing.
		'''
		if isinstance(values, list) and len(self) == len(values):
			i = 0
			for v in values:
				self[i].set_value(self[i].get_value() + v)
				i=i+1
			return True

		if not isinstance(values, list):
			for c in self:
				c.set_value(c.get_value() + values)

	def sub(self, values):
		if isinstance(values, list) and len(self) == len(values):
			i = 0
			for v in values:
				self[i].set_value(self[i].get_value() - v)
				i=i+1
			return True

		if not isinstance(values, list):
			for c in self:
				c.set_value(c.get_value() - values)

	def div(self, values):
		if isinstance(values, list) and len(self) == len(values):
			i = 0
			for v in values:
				self[i].set_value(self[i].get_value() / v)
				i=i+1
			return True

		if not isinstance(values, list):
			for c in self:
				c.set_value(c.get_value() / values)


	def mul(self, values):
		'''
		Multiply all the values in the list by the given value
		
		:param values: The value to multiply the vector by
		:return: Nothing.
		'''
		if isinstance(values, list) and len(self) == len(values):
			i = 0
			for v in values:
				self[i].set_value(self[i].get_value() * v)
				i=i+1
			return True

		if not isinstance(values, list):
			for c in self:
				c.set_value(c.get_value() * values)

	def exp(self, values):
		if isinstance(values, list) and len(self) == len(values):
			i = 0
			for v in values:
				self[i].set_value(self[i].get_value() ^ v)
				i=i+1
			return True

		if not isinstance(values, list):
			for c in self:
				c.set_value(c.get_value() ^ values)

	def is_number(self, s):
		try:
			float(s)
			return True
		except ValueError:
			return False

	def get_type(self):
		for c in self:
			if c is not None:
				if c.value.value is not None:
					if self.is_number(c.value.value) == False:
						return "text"

		return "number"

	def sum(self):
		result = 0
		for c in self:
			if c.value.value is not None:
				if self.is_number(c.value.value):
					result = float(result) + float(c.value.value)
		return result
		
	def get_unique_values(self):
		values = []
		for c in self:
			if (c.get_value() not in values):
				values.append(c.get_value())

		return (values)

	def as_array(self):
		values = []
		for c in self:
			values.append(c.get_value())
		return values
