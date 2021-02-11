import math

# Attempts to return the key "theta" from a point json object, otherwise 0
def extract_theta(pointData):
    try:
        return float(pointData["theta"])
    except KeyError:
        return 0

# y = theta, x = pixel center
# Applies an exponential regression to the pixel center to determine an approximation for the angle theta
# Note: more pixel and theta points would make this more accurate
def fit(center_x):   
    return 15.5068 * math.pow(math.e, 0.0047 * center_x)