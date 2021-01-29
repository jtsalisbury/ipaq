import json
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

def certain_distance(distance):

    for i, scan in enumerate(lidar.iter_scans()):
        #print("Quality: {q}\nAngle: {a}\nDistance: {d|\n\n".format(scan[i]['quality'], scan[i]['angle'], scan[i]['distance']))
        #print(scan[i])
        num = 0
        for blip in scan:
            #print(blip)
            if(int(blip[2]) >= distance):
                print("Distance: {}".format(str(blip[2])))
                num += 1
                y= blip[2]
                z = blip[1]
                #only return a range of thetas
                if (z >= 345 & z <= 45):
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
lidar.stop()
lidar.stop_motor()
lidar.disconnect()

quit()