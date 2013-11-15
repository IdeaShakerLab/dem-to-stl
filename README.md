DEM to STL
==========

This repository contains Python scripts for converting the CDED flavour of DEM (Digital Elevation Model) files to 2D Bitmaps and 3D STL files. CDED stands for Canadian Digital Elevation Model, and is generally used to describe topographical surveys of various regions within Canada. Example: [CDED Model of the Greater Toronto Area](http://geogratis.gc.ca/api/en/nrcan-rncan/ess-sst/d09e4699-94da-4e6d-bf65-4f3a55393606.html)

STL files are commonly used for 3D printing. The resulting STL files from this script should be fully 3D-printable.

## Basic Usage
These scripts were written and tested in Python 2.7.

Reading the DEM Metadata:
```
python dump_dem_metadata.py sourcefile.dem
```

Converting the DEM to a Bitmap:
```
python dem_to_bmp.py sourcefile.dem destinationfile.bmp [-c] [-q INT]
```
* The `-c` flag will output blue-green instead of greyscale.
* The `-q` represents "quality". 1 will match the source resolution, while higher numbers will reduce the resolution.

Converting the DEM to an STL:
```
python dem_to_stl.py sourcefile.dem destinationfile.stl [-q INT]
```
* The `-q` represents "quality". 1 will match the source resolution, while higher numbers will reduce the resolution.

## Advanced Usage

The module `cdedtools.demparser` currently offers two functions:
```python
from cdedtools import demparser

with open('filename.dem', 'r') as f:
  # read_metadata(f) will parse the headers of a DEM file
  # and return a dictionary of metadata entries. Integers
  # that represent string values in the CDED spec will be
  # translated to a readable string where appropriate, 
  # eg. uomGround: 1 -> uomGround: "Meters".
  # See cdedtools.translationtables to view all translations.
  metadata = demparser.read_metadata(f)
  
  # read_data(f) will parse the elevation data from a DEM
  # file and return a two-dimensional array of integers.
  # Typically, -32767 is considered a void value, while all
  # other values are distances above (+) or below (-) sea level.
  elevations = demparser.read_data(f)
```

The module `stltools.stlgenerator` offers a single function:
```python
from stltools import stlgenerator

heightmap = [
  [10, 10, 10], # y
  [10, 40, 10], # y
  [10, 10, 10]  # y
  # x,  x,  x
]

# Given a two-dimensional array of integers, this function
# will write a binary STL to the specified destination
# file. Under most circumstances, the model should be solid
# and manifold; ready for 3D printing. The heightmap is applied
# to the top facets only, while the bottom and sides will be flat.
# The distance between each point on the x and y axis will be 1mm.
# the elevation values will be interpreted in millimeters with 
# values less than 1 being rounded up to 1mm.
stlgenerator.generate_from_heightmap_array(heightmap, 'destination.stl')
```
