import numpy as np
from random import randrange
from time import sleep
import cv2
import keyboard
import math

# keep track of individual objects size and position while it exists on the field
class Obstacle():
    def __init__(self, size):
        self.size = size
        self.left = [0, 0]
        self.right = [0, 0]
        self.middle = [0, 0]
    
    def move(self, y, x):
        self.left = [self.left[0] + y, self.left[1] + x]
        self.right = [self.right[0] + y, self.right[1] + x]
        self.middle = [self.middle[0] + y, self.middle[1] + x]
        return
    
    def out_of_bounds(self, bounds):
        if(self.middle[0] >= bounds):
            return True
    

# currently set up to operate at same resolution as the realsense t265. This is only to match the relative size of recognized objects for get_objects()
# objects are created in a field (of the same size) above the visible field. This means if flying forward and full right/left no objects will be encountered.
# This could be solved a larger field. 
class VirtualDroneField():
    def __init__(self):
        self.y_lim = 800
        self.x_lim = 848
        self.drone = [round(self.y_lim/2), round(self.x_lim/2)]
        self.gen_field = np.zeros((self.y_lim, self.x_lim))
        self.detect_field = np.zeros((self.y_lim, self.x_lim))
        self.obstacles = []
        self.blips = []
    
    # this is the field that the drone views. The gen_field is where the obstacles are made beforehand
    def get_field(self):
        return self.detect_field
    
    # function that mimics the lidar scanning
    def get_blips(self):
        self.get_angles()
        return self.blips
    
    # function that mimics custom_object_detection.py object recognition
    def get_objects(self):
        objects = []
        for obstacle in self.obstacles:
            temp = {
                "object" : "tree", 
                "bbox_1" : [abs(obstacle.left[1]), abs(obstacle.left[0]-50)], 
                "bbox_2" : [abs(obstacle.right[1]), abs(obstacle.right[0]+50)]
            }
            objects.append(temp)
        return objects
    
    # this will add an obstacle to the field above the drone
    def add_random_obstacle(self):
        size = randrange(round(self.y_lim / 10), round(self.y_lim / 4))
        size = size % 2 + size
        start_point = randrange(size, self.x_lim - size)
        obstacle = Obstacle(size)
        temp = np.zeros((self.y_lim, self.x_lim))
        overlap = True
        while(overlap):
            count = 1
            for row in range(size*2 - 1):
                for column in range(count):
                    temp[self.y_lim - 1 - row, start_point+column] = 1
                if(row < size/2):
                    start_point -= 1
                    count += 2
                elif(row == obstacle.size/2):
                    obstacle.left = [-round(size/2)-1, start_point]
                    obstacle.right = [-round(size/2)-1, start_point+count-1]
                    obstacle.middle = [-round(size/2)-1, round(((count-1)/2) + start_point)]
                    start_point += 1
                    count -= 2
                elif(row >= size/2):
                    start_point += 1
                    count -= 2
            combined = temp + self.gen_field
            if(len(np.where(combined >= 2 , 1, 0).nonzero()) != 0):
                overlap = False
            else:
                temp = np.zeros((self.y_lim, self.x_lim)) # inefficient
        self.gen_field = temp + self.gen_field
        self.obstacles.append(obstacle)
        return
    
    # function that adds lines to the objects, making sure that there are none that exist behind another object
    def get_angles(self):
        blips = []
        angles = []
        for obstacle in self.obstacles:
            left_angle = math.degrees(math.atan2(obstacle.left[0]-self.drone[0], obstacle.left[1]-self.drone[1])) + 90
            right_angle = math.degrees(math.atan2(obstacle.right[0]-self.drone[0], obstacle.right[1]-self.drone[1])) + 90
            span = [degree for degree in range(round(left_angle), round(right_angle) +1)]
            distance = math.sqrt(math.pow((obstacle.middle[0]-self.drone[0]), 2) + math.pow((obstacle.middle[1]-self.drone[1]), 2))
            for degree in span:
                if(degree not in angles):
                    angles.append(degree)
                    blips.append({
                        "distance" : distance, 
                        "theta" : degree
                    })
        self.blips = blips
        return self.blips

    # remove obstacles that do not exist off the field
    def clean_obstacles(self):
        for obstacle in self.obstacles:
            if(obstacle.out_of_bounds(self.y_lim)):
                self.obstacles.remove(obstacle)
        return
    
    # position updates of obstacles for movement
    def update_obstacles(self, direction):
        (y, x) = direction
        self.clean_obstacles()
        for obstacle in self.obstacles:
            obstacle.move(y, x)
        return
    
    def move_up(self, amount):
        new_start = self.y_lim - amount 
        self.detect_field = np.vstack((self.gen_field, self.detect_field))[new_start : -amount, :]
        self.gen_field = np.vstack((np.zeros((amount, self.x_lim)), self.gen_field))[:-amount, :]
        self.update_obstacles((amount, 0))
        return
        
    def move_left(self, amount):
        self.detect_field = np.hstack((np.zeros((self.y_lim, amount)), self.detect_field[:, :-amount]))
        self.gen_field = np.hstack((np.zeros((self.y_lim, amount)), self.gen_field[:, :-amount]))
        self.update_obstacles((0, amount))
        return
        
    def move_right(self, amount):
        self.detect_field = np.hstack((self.detect_field[:, amount:], np.zeros((self.y_lim, amount))))
        self.gen_field = np.hstack((self.gen_field[:, amount:], np.zeros((self.y_lim, amount))))
        self.update_obstacles((0, -amount))
        return
    
    # draws a little drone in the middle, and converts the lidar scans to lines that are drawn 
    # image is returned as a numpy ndarray
    def get_image(self):
        image = np.copy(self.get_field())
        start = (self.drone[1], self.drone[0])
        dal = round(self.y_lim * 0.012) #drone arm length
        drd = round(self.y_lim * 0.016) #drone rotor width
        image = cv2.line(image, (start[0]-dal, start[1]-dal), (start[0]+dal, start[1]+dal), (1, 1, 1), 5);
        image = cv2.line(image, (start[0]+dal, start[1]-dal), (start[0]-dal, start[1]+dal), (1, 1, 1), 5);
        
        image = cv2.circle(image, (start[0]+drd, start[1]+drd), 10, (1,1,1))
        image = cv2.circle(image, (start[0]+drd, start[1]-drd), 10, (1,1,1))
        image = cv2.circle(image, (start[0]-drd, start[1]+drd), 10, (1,1,1))
        image = cv2.circle(image, (start[0]-drd, start[1]-drd), 10, (1,1,1))
        
        self.get_angles()
        for blip in self.blips:
            end_x = round(blip["distance"] * math.cos(math.radians(blip["theta"]-90))) + start[0]
            end_y = round(blip["distance"] * math.sin(math.radians(blip["theta"]-90))) + start[1]
            color = (1, 1, 1)
            image = cv2.line(image, start, (end_x, end_y), color, 1)
        return image

if __name__ == "__main__":
    vdf = VirtualDroneField()
    i = 0
    while(True):
        cv2.namedWindow("VirtualDrone", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("VirtualDrone", (vdf.get_image()))
        cv2.waitKey(5)
        if keyboard.is_pressed('left'):
            vdf.move_left(4)
        if keyboard.is_pressed('right'):
            vdf.move_right(4)
        vdf.move_up(4)
        
        if i % round(vdf.y_lim / 30) == 0:
            objects = vdf.get_objects()
            vdf.add_random_obstacle()
        
        #sleep(.2)
        i += 1