from imageai.Detection.Custom import DetectionModelTrainer

import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="objects")
trainer.setTrainConfig(object_names_array=["tree", "pole", "evergreen_tree"], batch_size=4, num_experiments=1000, train_from_pretrained_model="models\\pretrained-yolov3.h5")

trainer.trainModel()
