#function to find closest object
#import json
from rplidar import RPLidar
# Linux "/dev/ttyUSB0"
# Windows: "COM3"

class LIDAR:
    def __init__(self, port):
        self.port = port
       

    def start(self):
        self.lidar = RPLidar(self.port)
        # if(self.lidar.motor):
        #     self.lidar.stop()
        #     self.lidar.stop_motor()
        #     self.lidar.disconnect()
        info = self.lidar.get_info()
        health = self.lidar.get_health()
        print(info)
        print(health)

    def stop(self):
        self.lidar.stop()
        self.lidar.stop_motor()
        self.lidar.disconnect()

    def list_of_points(self, thetaLeft, thetaRight):
        array = []

        scanNum = 0
        for scan in enumerate(self.lidar.iter_scans()):
            scanNum = scanNum + 1
            print("Got " + str(len(scan[1])) + " points")
            for blip in scan[1]:
                theta = blip[1]

                if (theta > thetaLeft or theta < thetaRight):
                    point = {'distance': blip[2], 'theta': blip[1]}
                    array.append(point)

            if (scanNum >= 99):
                print("Ran too many scans, stopping!")
                self.stop()
                return []

            if (len(array) > 0):
                return array
            
if __name__ == "__main__":
    lidar = RPLidar("COM3")
    lidar.stop()
    lidar.stop_motor()
    lidar.disconnect()
