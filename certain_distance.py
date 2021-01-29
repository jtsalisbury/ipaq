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

def certain_distance(distance):
    for i, scan in enumerate(lidar.iter_scans()):
        for blip in scan:
            #print(blip)
            if(int(blip[2]) <= distance):
                # print("Distance: {}".format(str(blip[2])))
                y= blip[2]
                z = blip[1]
                #only return a range of thetas
                if (blip[1] >= 315 or blip[1] <= 45):
                    setinput = {
                        "distance": y,
                        "theta": z
                        }
                    convert = json.dumps(setinput)
                    print(convert)
        
        #print('%d: Got %d measurments' % (i, len(scan)))
        #it is just breaking after 100 scans, will need to change this at some point with something
        if i > 100:
            break


certain_distance(3000)

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

quit()
