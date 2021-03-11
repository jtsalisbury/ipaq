#function to find closest object
#import json
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

#check to make sure LIDAR is stopped so it can start in correct position

if(lidar.motor == False):
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
    lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

def list_of_points(thetaLeft, thetaRight):
    array = []
    for scan in enumerate(lidar.iter_scans()):
        for blip in scan:
            theta = blip[1]

            if (theta > thetaLeft or theta < thetaRight):
                point = {'distance': blip[2], 'theta': blip[1]}
                array.append(point)

        return array

list_of_points([315, 180])

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

quit()