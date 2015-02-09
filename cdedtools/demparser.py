"""
demparser.py
This module contains functions that will parse the
CDED flavour of DEM files provided by the government
of Canada.
"""

from translationtables import CDED as translationTable

def read_metadata(f):
    """
    Read the metdata from Logical Record A of the
    DEM file 'f'. This data will be returned as a
    dictionary object.

    Example Usage:
        with open('filename.dem', 'r') as f:
            metadata = demparser.read_metdata(f)
            for key, value in metadata.iteritems():
                print("{0:30s}: {1}".format(key, str(value)))
    """
    def read_value(translation):
        value = f.read(translation["length"]).strip()
        if "ignore" in translation:
            value = "** Field Ignored **"
        if translation["description"] != None and value:
            try:
                value = translation["description"][int(value)]
            except IndexError:
                value = value + " ** Invalid Description **"
        return value

    f.seek(0)
    return {translation["name"]: read_value(translation) for translation in translationTable}


def read_data(f):
    """
    Read the elevation data from Logical Record B of
    the file 'f'. This data will be returned as a
    two-dimensional list to be interpreted as:
    [
        Y1:[X1, X2, ...Xn],
        Y2:[X1, X2, ...Xn],
        ...
        Yn:[X1, X2, ...Xn]
    ]
    """
    percentComplete = 0
    data         = list()
    blocksize    = 1024 # TODO: Is 1024 a standard block size for USGS?
    headerlength = 144  # True for all USGS DEM
    import pdb; pdb.set_trace()
    f.seek(blocksize + 12)
    width        = int(f.read(6).strip())
    metadata     = read_metadata(f)
    height       = int(metadata["rowCount"])
    remainder    = (blocksize-4) - (width * 6 + headerlength) % (blocksize-4)
    blocksPerRow = (width * 6 + 144 + remainder) / (blocksize-4)
    def read_row(rowNumber):
        row = list()
        f.seek(blocksize + (blocksPerRow * blocksize) * rowNumber)
        f.read(headerlength) # TODO: Do something with the headers.
        for i in range(((blocksize-4) - headerlength)/6):
            row.append(int(f.read(6)))
        f.read(4)
        for i in range(blocksPerRow - 2):
            for j in range((blocksize-4)/6):
                row.append(int(f.read(6)))
            f.read(4)
        for i in range(((blocksize-4) - remainder)/6):
            row.append(int(f.read(6)))
        return row

    for row in range(height):
        data.append(read_row(row))
        if int(float(row) / height * 100) != percentComplete:
            percentComplete = int(float(row) / height * 100)
            print("Parsing DEM... {0}% Complete".format(percentComplete))
    return data
    
def read_data_asc(f):
    """
    Read the elevation data from 
    the file 'f'. This data will be returned as a
    two-dimensional list to be interpreted as:
    [
        Y1:[X1, X2, ...Xn],
        Y2:[X1, X2, ...Xn],
        ...
        Yn:[X1, X2, ...Xn]
    ]
    """
    data         = list()
    
    header = True
    for line in f:
        if not header:
            line = line.strip() #strip all leading/trailing whitespace
            line_list = line.split(" ")
            float_list=[float(elem) for elem in line_list]
            data.append(float_list)
            
        elif "NODATA" in line: #indicates end of header
            header = False
            
    return data
