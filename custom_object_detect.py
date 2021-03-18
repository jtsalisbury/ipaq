from imageai.Detection.Custom import CustomObjectDetection
import tensorflow as tf
import pyrealsense2 as rs
import numpy as np
import cv2
import os

class Object_Detector():
    def __init__(self, objects_directory, ml_name):
        #physical_devices = tf.config.list_physical_devices('GPU') 
        #tf.config.experimental.set_memory_growth(physical_devices[0], True)
        
        self.detector = CustomObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(os.path.join(objects_directory, "models", ml_name))
        self.detector.setJsonPath(os.path.join(objects_directory, "json", "detection_config.json"))
        self.detector.loadModel()
        self.start()
        
    def start(self):
        self.pipeline = rs.pipeline()
        config = rs.config()
        self.pipeline.start(config)
        
    def end(self):
        self.pipeline.stop()
    
    def format_data(self, detections):
        data = []
        for detection in detections:
            data.append({'object' : detection['name'], "bbox_1" : detection['box_points'][0:2], "bbox_2" : detection['box_points'][2:4], "confidence" : round(detection['percentage_probability'])})
        return data
    
    def get_objects(self):
        #self.start()
        frames = self.pipeline.wait_for_frames()
        left_frame = frames.get_fisheye_frame(1)
        left_image = np.asanyarray(left_frame.get_data())
        rgb_left_image = np.stack((left_image,)*3, axis=-1)
        detection_image, detections = self.detector.detectObjectsFromImage(input_image=rgb_left_image, input_type="array", output_type="array", minimum_percentage_probability=30)   
        
        #self.end()
        return (detection_image, self.format_data(detections))
        
if __name__ == "__main__":
    objects_dir = os.path.join(os.getcwd(), "objects")
    object_detector = Object_Detector(objects_dir, "detection_model-ex-323--loss-0019.126.h5")
    for i in range(1000):
        (detection_image, objects) = object_detector.get_objects()
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', detection_image)
        cv2.waitKey(1)
        print(objects)
    object_detector.end()
