from data.Column import Column
from data.Columns import Columns
from data.Row import Row
from data.Cell import Cell
import xlsxwriter
import datetime
from texttable import Texttable

class Frame(list):

	def __init__(self):
		self.rows = self
		self.name = ""
		self.columns = Columns()

	def __repr__(self):
		return self.print()

	# Get a specific row
	def get_row(self, i):
		return(self.rows[i])

	# Return columns of the dataset
	def get_column_names(self):
		cols = []
		r = self[0]
		for c in r:
			cols.append(c.column.name)
		return cols

	# Get a column with all values
	def get_column(self, column_name):
		c = Column()
		c.name = column_name
		for r in self:
			c.append(r.get_by_column_name(column_name))
		return c

	def get_unique_values(self, column_name):
		values = []
		for r in self:
			if (r.get_by_column_name(column_name).value.value not in values):
				values.append(r.get_by_column_name(column_name).value.value)

		return (values)

	def get_columns(self):
		self.columns = []

		for c in self.get_column_names():
			self.columns.append(self.get_column(c))

		return self.columns

	def add_column(self, c):
		if len(c) != len(self) and len(self) != 0:
			print ('Length of dataset not equal')
			return False

		if len(self) == 0:
			for cell in c:
				dr = Row()
				dr.append(cell)
				self.append(dr)
		else:
			i = 0
			for cell in c:
				self[i].append(cell)
				i = i + 1

		return True

	# Adds a row object to the list of rows of the dataframe
	def add_row(self, r):
		nr = Row()

		for key in r:
			nc = Column()
			nc.name = key

			ncell = Cell()
			ncell.set_value(r[key])

			ncell.column=nc
			nr.append(ncell)

		self.append(nr)

	def get_unique_values(self, column_name):
		values = []
		for r in self:
			if (r.get_by_column_name(column_name).value.value not in values):
				values.append(r.get_by_column_name(column_name).value.value )

		return values

	# prints the dataframe
	def print(self, **kwargs):

		cols_width = []
		table = Texttable()
		for c in self.get_column_names():
			cols_width.append(10)

		table.add_row(self.get_column_names())
		for r in self:
			table.add_row(r.get_array())

		table.set_cols_width(cols_width)
		table_s = " %s\n%s" % (self.name, table.draw())


		return(table_s)



	# search the data frame and returns dataframe with the results
	def search(self, field, values):

		df = Frame()

		for r in self:
			for c in r:
				if c.column.name == field and c.value.value == values:
					df.append(r)

		return df

	# Returns a dataframe in wide format
	def wide(self, label_field, value_field, column_field):
		# Frame that we will use to return our results

		self.to_xlsx()
		
		ndf = Frame()
		# Store column names
		cols = []
		# Store entity name
		row_labels = []
		# Capture different column and entity names
		for r in self:
			for c in r:
				if c.column.name == column_field and c.value.value not in cols:
					cols.append(c.value.value)
				if c.column.name == label_field and c.value.value not in row_labels:
					row_labels.append(c.value.value)

		# Sort columns
		cols = sorted(cols)

		#Create rows in wide format
		for r in row_labels:
			nr = Row()
			nr.append(Cell(column=label_field,value=r))

			# Search for cells of entity and value
			rr = self.search(label_field, r)
			for rrr in rr:
				ncc = Cell()
				for c in rrr:
					if c.column.name == column_field:
						ncc.column.name = c.value.value

					if c.column.name == value_field:
						ncc.value.set(c.value.value)

				nr.add_cell(ncc)

			ndf.append(nr)

		return ndf

	def merge(self, data_frames):
		ndf = Frame()
		for df in data_frames:
			for r in df:
				ndf.append(r)
		return ndf

	# Save the dataset to excel
	def to_xlsx(self):
		d = datetime.datetime.now()
		wb = xlsxwriter.Workbook('{}-{}{}{}{}{}{}'.format(self.name, d.year, d.month, d.day, d.hour, d.minute, '.xlsx'))
		ws = wb.add_worksheet()

		i = 1
		j = 0

		for c in self.get_column_names():
			ws.write(i, j, c)
			j=j+1

		format = wb.add_format()
		format.set_bold()
		ws.set_row(0,j,format)

		i = 2
		for r in self:
		    j=0
		    for c in r:
		        ws.write(i,j, c.value.get())
		        j=j+1

		    i=i+1

		wb.close()
