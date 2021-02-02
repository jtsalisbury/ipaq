from imageai.Detection.Custom import DetectionModelTrainer
#import tensorflow
#import os

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="objects")
trainer.setTrainConfig(object_names_array=["tree", "pole"], batch_size=2, num_experiments=100, train_from_pretrained_model="models\\pretrained-yolov3.h5")
trainer.trainModel()