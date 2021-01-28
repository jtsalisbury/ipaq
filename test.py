from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

for i, scan in enumerate(lidar.iter_scans()):
    #print("Quality: {q}\nAngle: {a}\nDistance: {d|\n\n".format(scan[i]['quality'], scan[i]['angle'], scan[i]['distance']))
    for blip in scan:
        #print(blip[1])
        #print("Distance: {}".format(str(blip[2])))
        if(int(round(blip[1])) > 358):
            print("Distance: {}m".format(str(blip[2]/1000)))
    #print('%d: Got %d measurments' % (i, len(scan)))
    if i > 1000:
        break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

quit()