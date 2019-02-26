class Indicator:
	name = ''
	description = ''
	source = ''
	sourcenote = ''
	note = ''
	datasource = ''
	url = ''
	source_metadata = ''
	data = {}

	def as_json(self):
		return dict(
			name=self.name,
			description=self.description,
			source=self.source,
			sourcenote=self.sourcenote,
			note=self.note,
			datasource=self.datasource,
			url=self.url,
			source_metadata = self.source_metadata,
			data=self.data)
