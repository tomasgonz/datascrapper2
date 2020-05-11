from data.Row import Row
from data.Column import Column
from data.Value import Value

class Cell:

	def __init__(self, **kwargs):

		self.column = Column()
		self.value  = Value()

		if 'column' in kwargs:
			self.column.name = str(kwargs['column'])

		if 'value' in kwargs:

			if kwargs['value'] == "--":
				self.value.value = None
				return

			if kwargs['value'] == "n/a":
				self.value.value = None
				return

			self.value.value = kwargs['value']

	def __repr__(self):
		return str(self.get_value())

	def what_is_this(self, s):

		if s is None:
			return False
		
		if isinstance(s, int):		
			return "int"
		
		if isinstance(s, float):
			return "float"
		
		if isinstance(s, str):
			return "str"

	def set_value(self, v):		

		if self.what_is_this(v) == "float":			 
			self.value.set(float(v))

		if self.what_is_this(v) == "int":
			self.value.set(int(v))
		
		if self.what_is_this(v) == "str":
			self.value.set(v)

	def get_value(self):
		return self.value.get()

	def print(self, kwargs):
		print (self.value.get())
