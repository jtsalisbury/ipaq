import math
import numpy as np

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
    return (center_x - 424) / 4.7267

def fitAng(ang):
    return 4.7267 * ang + 424