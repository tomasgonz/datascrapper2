from data.Frame import Frame
from data.Row import Row
from data.Cell import Cell
from data.Utils import is_number

def calculate_weighted_average(df_data, df_weight, label_field):

	df_w = Frame()

	# Go through all data rows
	for d in df_data.rows:
		dr = Row()
		# Now search data for weights based in the label field
		# We have to also search in a row for the label_field
		# and just the first result as the list will only contain
		# one value
		dr.add_cell(Cell(column=label_field,
						 value=d.get_cell(label_field).value.value))
		# If we are in a column that is not the label column
		# Now we go through all columns
		for c in d.cells:
			if c.column.name != label_field:
				data_value = d.get_cell(c.column.name).value.value

				dr.add_cell(Cell(column="%s_%s" % (c.column.name, 'value'),
								 value=data_value))

				# in the new row we have already created the label field that we
				# can use here
				# We have to check that the data point exists for the value that we are trying to weight
				if (len(df_weight.search(label_field,
												dr.get_cell(label_field).value.value).rows) > 0):
					weight_value = df_weight.search(label_field,
													dr.get_cell(label_field).value.value).rows[0].get_cell(c.column.name).value.value
				else:
					weight_value= None

				if data_value is None or weight_value is None:
					data_value = None
					weight_value = None

				dr.add_cell(Cell(column="%s_%s" %
								 (c.column.name, 'weight'), value = weight_value))

				# We will store the weighted value here

				dr.add_cell(Cell(column="%s_%s" %
								 (c.column.name, 'weighted_value'), value = None))

		# We add a column where the weighted value will be stored
		df_w.rows.append(dr)

	# Now let's calculated the weighted values
	for d in df_data.rows:
		for c in d.cells:
			if c.column.name != label_field:
				# Initialize variables to avoid carried-over values
				# from previous iteration

				data_value = None
				weight_value = None
				weighted_value = None

				# Check if weight value exists for data point
				if len(df_weight.search(label_field, d.get_cell(label_field).value.value).rows) > 0:

					if c.value.value is not None and df_weight.search(label_field,
						d.get_cell(label_field).value.value).rows[0].get_cell(c.column.name).value.value is not None:

						data_value = c.value.value

					weight_value = df_weight.search(label_field,
						d.get_cell(label_field).value.value).rows[0].get_cell(c.column.name).value.value

					total_weight = df_w.get_column("%s_%s" % (c.column.name, 'weight')).sum()

					if data_value is not None and weight_value is not None:
						if is_number(data_value) == True and is_number(weight_value) == True:
							weighted_value = (float(weight_value) /
											  		float(total_weight)) * float(data_value)
						else:
							weighted_value = None
					else:

						weighted_value = None

				# If weight value does not exists for the data point
				else:
					weighted_value = None

				df_w.search(label_field,
					d.get_cell(label_field).value.value).rows[0].get_cell("%s_%s" % (c.column.name, 'weighted_value')).value.value = weighted_value


	dr = Row()
	dr.add_cell(Cell(column=label_field, value='Average'))

	for c in df_w.get_column_names():
		total_weight = None
		if df_weight.get_column(c).get_type() == 'number':
			total_weight = df_w.get_column(c).sum()
			dr.add_cell(Cell(column=c, value=float(total_weight)))

	df_w.rows.append(dr)

	df_w.id = df_data.id + " - " + df_weight.id
	df_w.description = df_data.description + " weighted against " + df_weight.description 
	df_w.source = df_data.id + " : " + df_data.source + " and " + df_weight.id + " : " + df_weight.source
	df_w.source_url = df_data.id + " : " + df_data.source_url + " and " + df_weight.id + " : " + df_weight.source_url

	return df_w
