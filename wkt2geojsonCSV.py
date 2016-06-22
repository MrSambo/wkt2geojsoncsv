#!/usr/bin/python

import csv
import sys
import shapely.wkt
import geojson

csv.field_size_limit(sys.maxsize)

input_filename = sys.argv[1]
output_filename = sys.argv[2]


csvfile = open(input_filename, 'rb')
reader = csv.DictReader(csvfile)

# Rename WKT field (which is 1st field) to GeoJSON
reader.fieldnames[0] = 'GeoJSON'

c = csv.DictWriter(open(output_filename, "wb"), fieldnames=reader.fieldnames)
c.writeheader()

for row in reader:
    for col in row:
        if col == 'WKT':
            d_wkt = row['WKT']
            js1 = shapely.wkt.loads(d_wkt)
            js2 = geojson.Feature(geometry=js1, properties={})
            row['WKT'] = js2.geometry

    c.writerow(row)

print "%s >>> %s" % (input_filename, output_filename)