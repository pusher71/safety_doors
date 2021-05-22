from imageai.Detection import ObjectDetection
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "image.jpeg"),
                                             output_image_path=os.path.join(execution_path, "imagenew.jpeg"))

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"])
