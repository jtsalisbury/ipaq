from imageai.Detection.Custom import CustomObjectDetection
import pyrealsense2 as rs
import numpy as np
import cv2
import os

class Object_Detector():
    def __init__(self, objects_directory):
        self.pipeline = rs.pipeline()
        config = rs.config()
        self.pipeline.start(config)
        
        self.detector = CustomObjectDetection()
        self.detector.setModelTypeAsYOLOv3()
        self.detector.setModelPath(os.path.join(objects_directory, "models", "detection_model-ex-085--loss-0014.216.h5"))
        self.detector.setJsonPath(os.path.join(objects_directory, "json", "detection_config.json"))
        self.detector.loadModel()
        
    def end(self):
        self.pipeline.stop()
    
    def format_data(self, detections):
        data = []
        for detection in detections:
            data.append({'object' : detection['name'], "bbox_1" : detection['box_points'][0:2], "bbox_2" : detection['box_points'][2:4], "confidence" : round(detection['percentage_probability'])})
        return data
    
    def get_objects(self, display_window):
        frames = self.pipeline.wait_for_frames()
        left_frame = frames.get_fisheye_frame(1)
        left_image = np.asanyarray(left_frame.get_data())
        rgb_left_image = np.stack((left_image,)*3, axis=-1)
        detection_image, detections = self.detector.detectObjectsFromImage(input_image=rgb_left_image, input_type="array", output_type="array", minimum_percentage_probability=30)   
        if(display_window):
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', detection_image)
            cv2.waitKey(1)
        return self.format_data(detections)
        
if __name__ == "__main__":
    objects_dir = os.path.join(os.getcwd(), "objects")
    object_detector = Object_Detector(objects_dir)
    for i in range(100):
        objects = object_detector.get_objects(True)
        print(objects)
    object_detector.stop()
