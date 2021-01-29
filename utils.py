# Attempts to return the key "theta" from a point json object, otherwise 0
def extract_theta(pointData):
    try:
        return float(pointData["theta"])
    except KeyError:
        return 0

# Attempts to return the key "offset_x" from an image json object, otherwise 0
def extract_offset(objData):
    try:
        return float(objData["offset_x"])
    except KeyError:
        return 0