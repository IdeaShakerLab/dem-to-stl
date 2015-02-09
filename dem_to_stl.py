#!/usr/bin/env python

"""
This program will generate a binary STL file with
a variable number of facets.
"""

from cdedtools import demparser
from stltools  import stlgenerator

import argparse

# Command Line Options
parser = argparse.ArgumentParser(description="Generate an STL from a DEM file.")
parser.add_argument("-q", "--quality", dest="quality", default=2, help="The resolution of the resulting BMP. 1 will match the source resolution.")
parser.add_argument("sourcefile",  help="Read data from SOURCEFILE", metavar="SOURCEFILE")
parser.add_argument("destination", help="Save the resultion Bitmap file as DESTINATION", metavar="DESTINATION")
args = parser.parse_args()

filetype = args.sourcefile[-3:]

# Open the file and process the data
with open(args.sourcefile, "r") as f:
    if filetype == 'asc':
        print 'asc filetype'
        heightmap  = demparser.read_data_asc(f)
    else:
        heightmap  = demparser.read_data(f)
    resolution = int(args.quality)**2
    heightmap  = heightmap[::resolution]
    for y in range(len(heightmap)):
        heightmap[y] = heightmap[y][::resolution]
        heightmap[y] = heightmap[y][::-1]
        for x in range(len(heightmap[y])):
            heightmap[y][x] = heightmap[y][x] / 4 / float(resolution)
            if heightmap[y][x] < 1:
                heightmap[y][x] = 1
    stlgenerator.generate_from_heightmap_array(heightmap, args.destination)
