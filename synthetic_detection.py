from random import randrange
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
import math
import utils
class Synthetic_Detector():
    def __init__(self):
        object_type = "tree"
        self.bounds = [848, 800] # this might be backwards
        self.bbox_1 = []
        self.bbox_2 = []
        self.data = {"object" : object_type, "bbox_1" : [], "bbox_2" : [], "confidence" : 0}
        
    def get_data(self):
        self.data["bbox_1"] = self.bbox_1
        self.data["bbox_2"] = self.bbox_2
        self.data["confidence"] = randrange(30, 100)
        return self.data
    
    def get_objects(self, display_output):
        #returns a box that is between 10% and 25% of the 
        x_2 = randrange(round(self.bounds[0]/10), round(self.bounds[0]/4))
        y_2 = randrange(round(self.bounds[1]/10), round(self.bounds[1]/4))
        
        x = randrange(0, self.bounds[0] - x_2)
        y = randrange(0, self.bounds[1] - y_2)
        
        self.bbox_1 = [x, x_2]
        self.bbox_2 = [y, y_2]
        if(display_output):
            self.display_window()
        return self.get_data()

    # Note ang must be in degrees, will convert to radians
    def get_object_at_ang(self, ang):
        w = randrange(50, 100)
        h = randrange(50, 100)
        
        middleX = self.bounds[0] / 2

        xPos = utils.fitAng(ang)
        if ang < 0:
            center_x = middleX - (xPos - middleX)
        else:
            center_x = xPos

        center_y = round(self.bounds[1] / 2)

        self.bbox_1 = [round(center_x - w/2), round(center_y - h/2)]
        self.bbox_2 = [round(center_x + w/2), round(center_y + h/2)]

        return self.get_data()

    def display_window(self):
        fig, ax = plt.subplots()
        ax.plot([self.bounds[0],0], [0, self.bounds[1]])
        ax.add_patch(Rectangle((self.bbox_1[0], self.bbox_1[1]), self.bbox_2[0], self.bbox_2[0], angle=0.0, fill=False))
        plt.show()
