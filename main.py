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

maxHeight = 10 # measured in meters, the maximum height our drone is allowed to fly
minHeight = 1 # measured in meters, the minimum height our drone should try and maintain

maximumCollisionDistance = 10 # measured in meters, any collisions whose distance is less than this value are counted, otherwise we ignore them for now

homeAngleError = .087 # radians, .087 rad = 5 degrees, how much leeway we give when we want to face home
homePositionLatError = 1 # note one degreee of lat is approx 364,000 ft or 110947.2 meters
homePositionLongError = 1 # note one degree of long is approx 288,200 ft or 87843.36 meters

def getDistToGround():
    return 3

# Returns a list of "hits" from a predefined range
def getLidarSnapshot(): # dist in meters, theta in degrees
    points = [
        {
            "distance": 0.00000,
            "theta": 0.00000
        },
        {
            "distance": 0.0000,
            "theta": 0.0000
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
            
            # Off center left indicated by offset > 0, therefore we gotta set the angle
            if (obj["offset_x"] > 0):
                obj["theta"] = -1 * utils.fit(obj["offset_x"])
            else:
                obj["theta"] = utils.fit(obj["offset_x"])

            validObjects.insert(obj)

    # Sort objects so they appear in order from left to right
    validObjects.sort(key=utils.extract_theta, reverse=True)

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
            "distance": math.pow(center_x, 2) + math.pow(center_y, 2),
            "theta": theta
        })

    clusters.sort(key=utils.extract_theta)

    # loop through the clusters and assign them to objects!
    # note that this inheritely has many issues (and is a bad approach) if objects and clusters don't exactly equal
    # TODO: try to match objects and clusters based on theta and not where they are left to right
    collisions = []
    i = 0
    for cluster in clusters:
        if (objects[i]): # if we even have a corresponding image object
            cluster["imageObject"] = objects[i]
            i = i + 1
        
        # always just insert the cluster
        collisions.insert(cluster)

    return collisions 

def canMoveUp():
    return getDistToGround() < maxHeight

def canMoveDown():
    return getDistToGround() > minHeight

# Determine how far up we can go. This is either the min movement distance (if possible) or the remaining distance that's less than movementDistance
def getMoveDistanceUp():
    return curHeight + flyservice.movementDistance < maxHeight and flyservice.movementDistance or maxHeight - curHeight

# Determine how far up we can down. This is either the min movement distance (if possible) or the remaining distance that's less than movementDistance
def getMoveDistanceDown():
    return curHeight - flyservice.movementDistance > minHeight and flyservice.movementDistance or curHeight - minHeight

def collisionWithinReach(collision):
    return collision["distance"] <= maximumCollisionDistance

# Returns True or the angle required to face home
def isFacingHome():
    curAngle = flyservice.getAngle()
    curPos = flyservice.getPosition()

    targetPos = flyservice.getDestinationPosition()

    dX = targetPos["long"] - curPos["long"]
    dY = targetPos["lat"] - curPos["lat"]

    targetAngle = math.atan2(dY, dX)

    angDif = targetAngle - curAngle

    if (abs(angDif) < homeAngleError):
        return True
    
    return angDif

def faceHome(angleRotation):
    if (angleRotation < 0):
        flyservice.turnRight(angleRotation)
    else:
        flyservice.turnLeft(angleRotation)

homePositionLatError = 1 # note one degreee of lat is approx 364,000 ft or 110947.2 meters
homePositionLongError = 1 # note one degree of long is approx 288,200 ft or 87843.36 meters
def isHome():
    curPos = flyservice.getPosition()
    targetPos = flyservice.getDestinationPosition()

    # convert from long and lat to meters
    dX = (targetPos["long"] - curPos["long"]) * 87843.36
    dY = (targetPos["lat"] - curPos["lat"]) * 110947.2

    return abs(dX) <= homePositionLatError and abs(dy) <= homePositionLongError

# TODO: shutdown drone, account for camera being higher than drone landing pads
# note: future improvement, camera to check for collisions while landing
def land():
    flyservice.moveDown(getDistToGround())

while True:
    collisions = getPotentialCollisions()

    if (isHome()):
        land()
    
    # Attempt to turn towards our destination
    if (collisions.count == 0):
        angHome = isFacingHome()

        if (angHome != True):
            faceHome(angHome)

    # At this point we should really only be dealing with collisions that are within our drone's bounds
    shouldMoveForward = True
    for collision in collisions:
        if (collisionWithinReach(collision)): 
            if (canMoveUp()):
                flyservice.moveUp(getMoveDistanceUp())
            elif (canMoveDown()):
                flyservice.moveDown(getMoveDistanceDown())
            else:
                print("I seem to be stuck!")

            shouldMoveForward = False

    # TODO: some sort of logic to say "if we've gone all the way up, and all the way down, let's turn and try going around"

    if (shouldMoveForward):
        flyservice.moveForward()

    time.sleep(loopDelay)