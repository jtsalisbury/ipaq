from imageai.Detection.Custom import CustomObjectDetection
import pyrealsense2 as rs
import numpy as np
import cv2
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
print(os.path.join(execution_path, "objects", "models", "detection_model-ex-012--loss-0020.310.h5"))
print(os.path.join(execution_path, "objects", "json", "detection_config.json"))

detector.setModelPath(os.path.join(execution_path, "objects", "models", "detection_model-ex-012--loss-0020.310.h5"))
detector.setJsonPath(os.path.join(execution_path, "objects", "json", "detection_config.json"))
detector.loadModel()

#custom = detector.CustomObject(tree=True, pole=True)

pipeline = rs.pipeline()
config = rs.config()
pipeline.start(config)

try:
    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        #depth_frame = frames.get_depth_frame()
        left_frame = frames.get_fisheye_frame(1)
        #right_frame = frames.get_fisheye_frame(2)

        # Convert images to numpy arrays
        #depth_image = np.asanyarray(depth_frame.get_data())
        left_image = np.asanyarray(left_frame.get_data())
        rgb_left_image = np.stack((left_image,)*3, axis=-1)
        #right_image = np.asanyarray(right_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        #depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Stack both images horizontally
        
        detector_image, detections = detector.detectObjectsFromImage(input_image=rgb_left_image, input_type="array", output_type="array", minimum_percentage_probability=30)
        images = np.hstack((rgb_left_image, detector_image))
        for eachObject in detections:
            print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
            print("--------------------------------")
        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', images)
        cv2.waitKey(1)

finally:

    # Stop streaming
    pipeline.stop()
    
    
# detections = detector.detectCustomObjectsFromImage( custom_objects=custom, input_image=os.path.join(execution_path , "image3.jpg"), output_image_path=os.path.join(execution_path , "image3new-custom.jpg"), minimum_percentage_probability=30)