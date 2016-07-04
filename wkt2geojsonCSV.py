#!/usr/bin/python

import csv
import sys
import shapely.wkt
import geojson

csv.field_size_limit(sys.maxsize)

input_filename = sys.argv[1]
output_filename = "parsed_output/" + sys.argv[1]


csvfile = open(input_filename, 'rb')
reader = csv.DictReader(csvfile)

# Rename the_geom field to GeoJSON
# print "%s" % (reader.fieldnames[1]);
reader.fieldnames[1] = 'GeoJSON'

c = csv.DictWriter(open(output_filename, "wb"), fieldnames=reader.fieldnames)
c.writeheader()

for row in reader:
    for col in row:
        if col == 'GeoJSON':
            d_wkt = row['GeoJSON']
            js1 = shapely.wkt.loads(d_wkt)
            js2 = geojson.Feature(geometry=js1, properties={})
            row['GeoJSON'] = js2.geometry

    c.writerow(row)

print "%s >>> %s" % (input_filename, output_filename)