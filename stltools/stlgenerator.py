"""
A collection of functions to generate a 3D stl
model using various data sets.
"""

from struct      import pack
from writefacets import *

def generate_from_heightmap_array(heightmap, destination):
    # Pad the heightmap so that it joins the polygons
    # at the sides of the base.
    for row in heightmap:
        row.append(1)
        row.insert(0,1)
    heightmap.insert(0, [1 for x in heightmap[0]])
    heightmap.append(heightmap[0][:])

    percentComplete = 0
    height = len(heightmap) - 1
    width  = len(heightmap[0]) - 1
    with open(destination, 'w') as f:
        # Write the file header
        f.write(pack('80s', "Generic cube shape."))
        # Write the number of facets
        numTopBottomFacets = width * height * 4
        numNorthSouthFacets  = width * 4
        numEastWestFacets = height * 4
        f.write(pack('i', numTopBottomFacets + numNorthSouthFacets + numEastWestFacets))

        # Generate the bottom plane.
        for y in range(height):
            if int(float(y) / height * 100) != percentComplete:
                percentComplete = int(float(y) / height * 100)
                print("Writing STL File... {0}% Complete".format(percentComplete))
            writeEastFacet(f, 0, y, 0)
            writeWestFacet(f, width, y, 0)
            for x in range(width):
                if y == 0:
                    writeNorthFacet(f, x, y, 0)
                if y == height-1:
                    writeSouthFacet(f, x, y+1, 0)
                writeBottomFacet(f, x, y, 0)
                writeTopFacet(f, x, y, heightmap)

        # Finished writing to file
        f.close()
        print("File saved as: " + destination)
