#function to find closest object
import json
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

def closest_object():
    largest_dist = 0
    largest_angle = 0
    # largest = {'distance' : 0, 'theta' : 0}
    for i, scan in enumerate(lidar.iter_scans()):
        for blip in scan:
            #blip[1] = angle, blip[2]=distance
            if(int(round(blip[1])) > 315 or int(round(blip[1])) < 45):
                if(blip[2] > largest_dist):
                    largest_dist = blip[2]
                    largest_angle = blip[1]
            # print(largest_dist)
            largest = {'distance' : largest_dist, 'theta' : largest_angle}
            json_data = json.dumps(largest)
            print(json_data)
            # with open("sample.json", "w") as outfile: 
            #     json.dump(largest, outfile) 
        #just for testing purposes
        if i > 100:
            break

closest_object()

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

quit()
