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

dis_string = "Distance:"
def list_of_points(thetas):
    for scan in enumerate(lidar.iter_scans()):
        for blip in scan:
            for theta in thetas:
                if(int(round(blip[1])) == theta):
                    points = {'distance': blip[2]}
                    array.append(dis_string)
                    array.append(points)
                    print(array)
                # not sure why printing largest here?
                #json_data = json.dumps(largest)
                #print(json_data)
        if i > 100:
            break

list_of_points([315, 180])

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

quit()