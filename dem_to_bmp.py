#!/usr/bin/env python

"""
This program will generate a greyscale bitmap from a
CDED flavoured DEM file.
"""

from cdedtools import demparser

import argparse
import Image

# Command Line Options
parser = argparse.ArgumentParser(description="Generate a BMP from a DEM file.")
parser.add_argument("-c", "--colourize", dest="colourize", action="store_true", help="Add this flag to output blue-green instead of greyscale.")
parser.add_argument("-q", "--quality",   dest="quality",   default=1,           help="The resolution of the resulting BMP. 1 will match the source resolution.")
parser.add_argument("sourcefile",  help="Read data from SOURCEFILE", metavar="SOURCEFILE")
parser.add_argument("destination", help="Save the resultion Bitmap file as DESTINATION", metavar="DESTINATION")
args = parser.parse_args()

with open(args.sourcefile, 'r') as f:
    percentComplete = 0
    heightmap  = demparser.read_data(f)
    resolution = int(args.quality)**2
    heightmap  = heightmap[::resolution]
    height     = len(heightmap)
    width      = len(heightmap[0][::resolution])
    img        = Image.new('RGB', (width, height), '#00F')
    for y in range(len(heightmap)):
        if int(float(y) / len(heightmap) * 100) != percentComplete:
            percentComplete = int(float(y) / len(heightmap) * 100)
            print("Drawing Bitmap... {0}% Complete".format(percentComplete))
        heightmap[y] = heightmap[y][::resolution]
        heightmap[y] = heightmap[y][::-1]
        for x in range(len(heightmap[y])):
            colour = int(float(max(heightmap[y][x], 0)) / 500 * 255)
            if(args.colourize):
                img.putpixel((y,x), (0, colour, 100))
            else:
                img.putpixel((y,x), (colour, colour, colour))
    img.save(args.destination, 'BMP')
    print("Image saved as: {0}".format(args.destination))
