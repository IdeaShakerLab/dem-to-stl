"""
This module contains a series of lists used to map out the Record A
headers of various DEM format files. Each list contains dictionary
objects describing the length (in bytes), name, and possibly a
value translation (int to string) for all possible entries in
Logical Record A of the associated DEM format.
"""

CDED = [
    {"name":"fileName",                       "length":40, "description":None},
    {"name":"responsabilityCenter",           "length":60, "description":None},
    {"name":"filler",                         "length":9,  "description":None},
    {"name":"seGeographicCorner",             "length":26, "description":None},
    {"name":"softwareUsed",                   "length":1,  "description":[None, None, None, None, None, None, None, None, "ANUDEM", "FME for Linux"]},
    {"name":"filler",                         "length":1,  "description":None},
    {"name":"sectionalIndicator",             "length":3,  "description":None},
    {"name":"originCode",                     "length":4,  "description":None},
    {"name":"demLevelCode",                   "length":6,  "description":None},
    {"name":"elevationPattern",               "length":6,  "description":[None, 'Regular', 'Random']},
    {"name":"planimetricReferenceSystem",     "length":6,  "description":['Geographic', 'UTM', 'State Plane']},
    {"name":"zoneReferenceSystem",            "length":6,  "description":None},
    {"name":"mapProjectionParameters",        "length":360,"description":None, "ignore":True},
    {"name":"uomGround",                      "length":6,  "description":['Radians', 'Meters', 'Feet', 'Arc Seconds']},
    {"name":"uomElevation",                   "length":6,  "description":[None, 'Feet', 'Meters']},
    {"name":"quadrangleSideCount",            "length":6,  "description":None},
    {"name":"quadrangleCoordinatesArray",     "length":192,"description":None},
    {"name":"minMaxElevations",               "length":48, "description":None},
    {"name":"counterclockwiseAngle",          "length":24, "description":None},
    {"name":"elevationAccuracy",              "length":6,  "description":['Accuracy Unknown', 'Accuracy given in Record C']},
    {"name":"xyzResolution",                  "length":36, "description":None},
    {"name":"collumnCount",                   "length":6,  "description":None},
    {"name":"rowCount",                       "length":6,  "description":None},
    {"name":"largestPrimaryContourInterval",  "length":5,  "description":None},
    {"name":"counterIntervalUnits",           "length":1,  "description":['N/A', 'Feet', 'Meters']},
    {"name":"smallestPrimaryContourInterval", "length":5,  "description":None},
    {"name":"counterIntervalUnits",           "length":1,  "description":['N/A', 'Feet', 'Meters']},
    {"name":"dataSourceDate",                 "length":4,  "description":None},
    {"name":"dataRevisionDate",               "length":4,  "description":None},
    {"name":"inspectionFlag",                 "length":1,  "description":None},
    {"name":"validationFlag",                 "length":1,  "description":['Not Validated', 'Validated', 'Validated', 'Validated', 'Validated', 'Validated']},
    {"name":"suspectVoidAreasFlag",           "length":2,  "description":['No Suspect/Void Areas', 'Suspect Areas', 'Void Areas', 'Both Suspect and Void Areas']},
    {"name":"verticalDatum",                  "length":2,  "description":[None, 'Local Mean Sea Level', 'NGVD 29', 'NAVD 88']},
    {"name":"horizontalDatum",                "length":2,  "description":[None, 'North American Datum 1927', 'World Geodetic System 1972', 'WGS 84', 'NAD 83', 'Old Hawaii Datum', 'Puerto Rico Datum']},
    {"name":"dataEdition",                    "length":4,  "description":None},
    {"name":"percentVoid",                    "length":4,  "description":None},
    {"name":"edgeMatchFlag",                  "length":8,  "description":None},
    {"name":"verticalDatumShift",             "length":7,  "description":None},
]
