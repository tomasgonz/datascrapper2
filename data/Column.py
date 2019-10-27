class Column(list):

	def __init__(self):
		self.name = ""
		# Collection of all values of the column
		pass

	def add(self, values):
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
		if isinstance(values, list) and len(self) == len(values):
			i = 0
			for v in values:
				self[i].set_value(self[i].get_value() * v)
				i=i+1
			return True

		if not isinstance(values, list):
			for c in self:
				c.set_value(c.get_value() * values)

	def exp(self):
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

	def get_as_array(self):
		values = []
		for c in self:
			values.append(c.get_value())
		return values
