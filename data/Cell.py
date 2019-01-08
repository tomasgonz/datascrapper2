from data.Row import Row
from data.Column import Column
from data.Value import Value

class Cell:
	
	def __init__(self, **kwargs):				

		self.column = Column()
		self.value  = Value()

		if 'column' in kwargs:
			self.column.name = kwargs['column']

		if 'value' in kwargs:

			if kwargs['value'] == "--":
				self.value.value = None
				return

			if kwargs['value'] == "n/a":
				self.value.value = None
				return
			
			self.value.value = kwargs['value']
	
	def is_number(self, s):

		if s is None: 
			return False					
		try:
			float(s)
			return True
		except ValueError:
			return False

	def set_value(self, v):		

		if self.is_number(v):			
			self.value.set(float(v))
		else:
			self.value.set(v)
		
	def get_value(self):
		return self.value.get()

	def print(self, kwargs):				
		print (self.value.get())