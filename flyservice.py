movementDistance = 1 # measured in meters, how far we should try and move on each iteration

def getDestinationPosition():
    return {
        "lat": 39, # y
        "long": -84 # x
    }

def getPosition():
    return {
        "lat": 100, # y
        "long": 20 # x
    }

# only return the angle relative to the forward direction
# this should return in radians
# this should also increase from the +x counter clockwise
def getAngle():
    return 1.5 # rad

def moveUp(distance):
    print("Moving up " + str(distance))

    return 1

def moveDown(distance):
    print("Moving down " + str(distance))

    return 2

# ang is in radians, increases counter clockwise from the +x
def turnLeft(ang):
    return 3

# ang is in radians, increases counter clockwise from the +x
def turnRight(ang):
    return 3

def moveForward(distance):
    print("Moving forward " + str(distance))

    return 4