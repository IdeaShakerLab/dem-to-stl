DEM to STL
==========

This repository contains Python scripts for converting the CDED flavour of DEM (Digital Elevation Model) files to 2D Bitmaps and 3D STL files. CDED stands for Canadian Digital Elevation Model, and is generally used to describe topographical surveys of various regions within Canada. Example: [CDED Model of the Greater Toronto Area](http://geogratis.gc.ca/api/en/nrcan-rncan/ess-sst/d09e4699-94da-4e6d-bf65-4f3a55393606.html)

STL files are commonly used for 3D printing. The resulting STL files from this script should be fully 3D-printable.

## Basic Usage
These scripts were written and tested in Python 2.7.

Reading the DEM Metadata:
`python dump_dem_metadata.py sourcefile.dem`

Converting the DEM to a Bitmap:
`python dem_to_bmp.py sourcefile.dem destinationfile.bmp [-c] [-q INT]`
* The `-c` flag will output blue-green instead of greyscale.
* The `-q` represents "quality". 1 will match the source resolution, while higher numbers will reduce the resolution.

Converting the DEM to an STL:
`python dem_to_stl.py sourcefile.dem destinationfile.stl [-q INT]`
* The `-q` represents "quality". 1 will match the source resolution, while higher numbers will reduce the resolution.
