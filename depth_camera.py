import pyrealsense2 as rs
import numpy as np


class Depth_Finder():
    def __init__(self):
        self.pipeline = rs.pipeline()
        config = rs.config()
        self.pipeline.start(config)
        
    def end(self):
        self.pipeline.stop()
    
    def get_most_shallow(self):
        frame = self.pipeline.wait_for_frames()
        depth_frame = frame.get_depth_frame()
        #depth_image = np.asanyarray(depth_frame.get_data())
        #rgb_depth_image = np.stack((depth_image,)*3, axis=-1)
        low = 9999
        for x in range(depth_frame.width):
            for y in range(depth_frame.height):
                distance = depth_frame.get_distance(x, y)
                if(distance != 0 and distance < low):
                    low = distance
        print(low)
        return low
