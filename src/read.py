from avro.datafile import DataFileReader
from avro.io import DatumReader
import sys

reader = DataFileReader(open(sys.argv[1], "r"), DatumReader())
count = 0
for line in reader:
	print(line)
	count += 1
reader.close()
print("Count: %d" % count)