================
csv2avro
================

Command line script to convert CSV/TSV files to AVRO

================
Usage
================

	usage: csv2avro.py [-h] [--dialect DIALECT] in_file out_file

	csv2avro.py: error: too few arguments

Default dialect = 'excel-tab' - default python dialects are supported.

================
Example
================

	python src/csv2avro.py examples/example.csv examples/example.avro --dialect excel

This will convert the example.csv into example.avro, which you can then read and verify has the same rows/content as you expect using the provided src/read.py:

	python src/read.py examples/example.avro

	{u'food': u'Pizza', u'name': u'Mike'}

	{u'food': u'Pie', u'name': u'Ben'}

	{u'food': u'Burgers', u'name': u'John'}
	
	Count: 3
	
To learn more about why I wrote this utility, see my blog post: http://garrens.com/blog/2015/03/21/converting-csvs-with-headers-to-avro/
