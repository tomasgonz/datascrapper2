class Row(list):

	def __init__(self, **kwargs):
		self.cells = self

	def add_cell(self, c):
		self.cells.append(c)

	def print(self):
		print (' '.join("|{}|".format(c.value.value) for c in self.cells))

	def get_columns(self):
		cs = []
		for c in self.cells:
			cs.append(c.column)
		return cs

	def get_column_names(self):
		cs = []
		for c in self.cells:
			cs.append(c.column.name)
		return cs

	def get_cell(self, column_name):
		for c in self.cells:
			if c.column.name == column_name:
				return c

	def as_array(self):
		r = []

		for c in self.cells:
			r.append(c.value.value)

		return(r)

	def search(self, field, value):
		result_cells = []
		for c in self.cells:
			if c.column.name == field and c.value.value == value:
				result_cells.append(c)

		return result_cells

	def as_json(self):
		row_data = {}
		
		for c in self.cells:
			row_data[c.column.name] = c.value.value
		
		return row_data
	
