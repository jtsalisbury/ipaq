import time
import math

from sklearn.cluster import DBSCAN
from sklearn import preprocessing

import flyservice
import utils

# Note: Critically important that the front-facing camera and lidar are pointing directly ahead
#       Further, they should be placed at the same angle and directly above or below each other

loopDelay = 1   # second delay between loop iterations
droneWidth = 1  # measured in meters, how wide the drone is, to accurately determine potential collisions

moduleOffset = 0 # measured in meters, how far left (negative) or right (positive) the equipment is mounted on the drone
distBetweenLidarCamera = 0 # measured in meters, how far away the the lidar is from the camera. Negative: camera below lidear, positive: camera above lidar

# Max resolution of the front-facing camera
cameraResolution = {
    "x": 848,
    "y": 800
}

cameraPixelOffset = 0 # how many pixels of freedom to give to potential collisions based off the center of the frame

def getDistToGround():
    return 3

# Returns a list of "hits" from a predefined range
def getLidarSnapshot(): # dist in meters, theta in degrees
    points = [
        {
            "distance": "0.00000",
            "theta": "0.00000"
        },
        {
            "distance": "0.00000",
            "theta": "0.00000"
        }
    ]

    return points

# Returns a list of objects in the camera FOV
def getCameraSnapshot():
    objects = [
        { 
            "object": "tree",
            "box_1": [20, 20],
            "box_2": [200, 200]
        }, 
        { 
            "object": "car",
            "box_1": [600, 600],
            "box_2": [840, 800]
        }
    ]

    return objects

# Returns a list of points that are in front of our drone
def getValidPoints():
    points = getLidarSnapshot()
    validPoints = []

    for point in points:
        angRad = point["theta"] * math.pi / 180    # convert angle to radians
        x = point["distance"] * math.sin(angRad)   # determine how far the point is from the direct center of our module 
        y = point["distance"] * math.cos(angRad)
        droneCenterOffset = moduleOffset      

        # 180 is arbitrary, just need to know if relative to forward, this point is on our left or right
        # this performs corrections on our points and makes sure we are only dealing with points relative to the center of the drone, not the lidar
        if point["theta"] > 180: # assuming this means we are on the left
            droneCenterOffset -= moduleOffset
            #point["theta"] = point["theta"] - 360 # make it negative so we can sort it (ie: 358 -> -2, so we can have -2, -1, 0, 1, 2, etc)

        # We only care about potential collisions that are within our drones bounding box
        if x + moduleOffset <= droneWidth / 2 + 0.5:
            validPoints.insert([x, y])

    #validPoints.sort(key=utils.extract_theta)

    return validPoints 

def getPointClusters(points):
    return DBSCAN(eps=0.5, min_samples=5, leaf_size=30).fit(points)

def getObjectsInPath():
    middleX = cameraResolution["x"] / 2
    middleY = cameraResolution["y"] / 2 # first, determine the center of our camera screen

    objects = getCameraSnapshot()

    validObjects = []

    for obj in objects:
        x1 = obj["box_1"][0] - cameraPixelOffset
        x2 = obj["box_2"][0] + cameraPixelOffset
        y1 = obj["box_1"][1] - cameraPixelOffset
        y2 = obj["box_2"][1] + cameraPixelOffset

        # Our middle point is within the bounding box of our detected object
        if (x1 <= middleX and x2 >= middleX and y1 <= middleY and y2 >= middleY):
            obj["middle_x"] = x2 - x1 / 2
            obj["middle_y"] = y2 - y1 / 2
            obj["offset_x"] = cameraResolution["x"] / 2 - obj["middle_x"] # positive x indicates box is off-center left, negative indicates box is off-center right

            validObjects.insert(obj)

    # Sort objects so they appear in order from left to right
    validObjects.sort(key=utils.extract_offset, reverse=True)

    return validObjects

def getPotentialCollisions():
    points = getValidPoints()
    clusters = getPointClusters(points)
    objects = getObjectsInPath()

    labels = clusters.labels_ 

    #todo i have no idea if this is right
    # but i want to create cluster centers 
    centerDict = {}
    i = 0
    for label in labels:
        if (centerDict[label]):
            centerDict[label] = {
                "x": centerDict[label]["x"] + points[i][0],
                "y": centerDict[label]["y"] + points[i][1],
                "pts": centerDict[label]["pts"] + 1
            }
        else:
            centerDict[label] = {
                "x": points[i][0],
                "y": points[i][1],
                "pts": 1
            }

        i = i + 1

    # clusters!
    clusters = []
    for label in centerDict:
        center_x = centerDict[label]["x"] / centerDict[label]["pts"]
        center_y = centerDict[label]["y"] / centerDict[label]["pts"]
        theta = math.atan(center_x / center_y) # relative to our module, note this is in radians

        clusters.insert({
            "center_x": center_x,
            "center_y": center_y,
            "theta": theta
        })

    clusters.sort(key=utils.extract_theta)

    # loop through the clusters and assign them to objects!
    # note that this inheritely has many issues (and is a bad approach) if objects and clusters don't exactly equal
    collisions = []
    i = 0
    for cluster in clusters:
        if (objects[i]): # if we even have a corresponding image object
            cluster["imageObject"] = objects[i]
            i = i + 1
        
        # always just insert the cluster
        collisions.insert(cluster)

    return collisions 


while True:
    collisions = getPotentialCollisions()

    time.sleep(loopDelay)