#!/usr/bin/env python

"""
Read a USGS Formatted DEM file, and produce basic file information.
The USGS DEM standard maps metadata concerning the topographical data to collumns
between bytes 1 and 915. The standard identifies the number of bytes within each
collumn, and these need to be explicitely mapped out in code for proper reading.
Each byte is ASCII formatting, allowing for fairly simple interpretation of data.
"""

from cdedtools import demparser

import argparse

# Command Line Options
parser = argparse.ArgumentParser(description="Dump the metadata from the headers of a DEM file.")
parser.add_argument("filename", help="Read data from FILE", metavar="FILE")
args = parser.parse_args()

# Open the file and process the data
with open(args.filename, "r") as f:
    print("-------------------------------------------------");
    metadata = demparser.read_metadata(f)
    for key, value in metadata.iteritems():
        print("{0:30s}: {1}".format(key, str(value)))
    print("-------------------------------------------------");
