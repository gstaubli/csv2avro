import csv
import argparse
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

parser = argparse.ArgumentParser(description='Convert CSV to Avro')
parser.add_argument('in_file',help='Path to CSV file with header')
parser.add_argument('out_file',help='Path to output AVRO file')
parser.add_argument('--dialect',help='CSV Dialect',default='excel-tab')
args = parser.parse_args()

def get_name_type_pairs(header):
	return ",\n".join(['\t\t{"name": "%s", "type": "string"}' % x for x in header])

def generate_schema(args,header):
	schema_str = """
{
	"namespace": "%s",
	"type": "record",
	"name": "Log",
	"fields": [
%s
	]
}""" % (args.out_file,get_name_type_pairs(header))
	return avro.schema.parse(schema_str)

with open(args.in_file,'r') as opened_in_file:
	reader = csv.DictReader(opened_in_file,dialect=args.dialect)
	header = reader.fieldnames
	avro_schema = generate_schema(args,header)
	with open(args.out_file,'w') as opened_out_file:
		writer = DataFileWriter(opened_out_file, DatumWriter(), avro_schema)
		for line in reader:
			try:
				writer.append(line)
			except Exception as e:
				print("Error: %s for line %s" % (e,line))
		writer.close()