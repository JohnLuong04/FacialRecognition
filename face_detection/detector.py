import cv2 as cv
import numpy as np
import dlib


class Detector:
    def __init__(self, prototxt_path, model_path, predictor_path, confidence_threshold = 0.5):
        self.net = cv.dnn.readNetFromCaffe(prototxt_path, model_path)
        self.conf_threshold = confidence_threshold

        self.predictor = dlib.shape_predictor(predictor_path)


    def detect(self, image):
        height, width = image.shape[:2]
        blob = cv.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
        self.net.setInput(blob)
        detections = self.net.forward()

        boxes = []
        eyes = []


        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.conf_threshold:
                box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
                (x1, y1, x2, y2) = box.astype("int")
                boxes.append((x1, y1, x2 - x1, y2 - y1))

                gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                rect = dlib.rectangle(x1,y1,x2,y2)
                shape = self.predictor(gray, rect)

                left_eye = [(shape.part(i).x, shape.part(i).y) for i in range(36, 42)]
                right_eye = [(shape.part(i).x, shape.part(i).y) for i in range(42, 48)]
                eyes.append((left_eye, right_eye))

        return boxes, eyes
