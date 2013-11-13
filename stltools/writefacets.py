"""
A collection of methods that will write a single polygonal facet
to a binary STL file.
"""

from struct import pack

def writeTopFacet(f, x, y, heightmap):
    # Normal - A
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', heightmap[y][x]))
    # Vertex 2
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', heightmap[y][x+1]))
    # Vertex 3
    f.write(pack('f', x + 1))
    f.write(pack('f', y + 1))
    f.write(pack('f', heightmap[y+1][x+1]))
    # End Facet
    f.write(pack('h', 0))
    # Normal - B
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x + 1))
    f.write(pack('f', y + 1))
    f.write(pack('f', heightmap[y+1][x+1]))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', heightmap[y+1][x]))
    # Vertex 3
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', heightmap[y][x]))
    # End Facet
    f.write(pack('h', 0))

def writeBottomFacet(f, x, y, z):
    # Normal - A
    f.write(pack('f', 0))
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x + 1))
    f.write(pack('f', y + 1))
    f.write(pack('f', z))
    # Vertex 3
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # End Facet
    f.write(pack('h', 0))
    # Normal - B
    f.write(pack('f', 0))
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z))
    # Vertex 3
    f.write(pack('f', x + 1))
    f.write(pack('f', y + 1))
    f.write(pack('f', z))
    # End Facet
    f.write(pack('h', 0))

def writeNorthFacet(f, x, y, z):
    # Normal - A
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # Vertex 3
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # End Facet
    f.write(pack('h', 0))
    # Normal - B
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 3
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # End Facet
    f.write(pack('h', 0))

def writeSouthFacet(f, x, y, z):
    # Normal - A
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # Vertex 3
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # End Facet
    f.write(pack('h', 0))
    # Normal - B
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # Vertex 3
    f.write(pack('f', x + 1))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # End Facet
    f.write(pack('h', 0))

def writeEastFacet(f, x, y, z):
    # Normal - A
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # Vertex 3
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z + 1))
    # End Facet
    f.write(pack('h', 0))
    # Normal - B
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z + 1))
    # Vertex 3
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z))
    # End Facet
    f.write(pack('h', 0))

def writeWestFacet(f, x, y, z):
    # Normal - A
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z + 1))
    # Vertex 3
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z + 1))
    # End Facet
    f.write(pack('h', 0))
    # Normal - B
    f.write(pack('f', 0))
    f.write(pack('f', -1))
    f.write(pack('f', 0))
    # Vertex 1
    f.write(pack('f', x))
    f.write(pack('f', y))
    f.write(pack('f', z))
    # Vertex 2
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z))
    # Vertex 3
    f.write(pack('f', x))
    f.write(pack('f', y + 1))
    f.write(pack('f', z + 1))
    # End Facet
    f.write(pack('h', 0))
