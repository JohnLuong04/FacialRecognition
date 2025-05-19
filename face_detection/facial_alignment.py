import os

import cv2
import cv2 as cv
import math
import numpy as np
import dlib

predictor_path = "face_detection/models/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

detector = dlib.get_frontal_face_detector()

image_path = 'database/initial_face_images/face1.png'
image = cv.imread(image_path, cv.IMREAD_UNCHANGED)

def average_eye_position(landmark, start, end):
    x_total, y_total = 0, 0
    for i in range(start, end):
        x_total += landmark.part(i).x
        y_total += landmark.part(i).y
    count = end - start
    return x_total / count, y_total / count


def facial_alignment(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)


    faces = detector(gray)
    landmark = predictor(gray, faces[0])

    left_x, left_y = average_eye_position(landmark, 36, 42)
    right_x, right_y = average_eye_position(landmark, 42, 48)

    dy = right_y - left_y
    dx = right_x - left_x

    angle = math.degrees(math.atan2(dy,dx))

    center_x = (left_x + right_x) // 2
    center_y = (left_y + right_y) // 2

    rot_matrix = cv.getRotationMatrix2D((center_x, center_y), angle, scale=1.0)
    aligned_image = cv.warpAffine(image, rot_matrix, (image.shape[1], image.shape[0]))

    return aligned_image

try:
    aligned = facial_alignment(image)
    cv.imshow("Aligned Face", aligned)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite("aligned_output.png", aligned)
except Exception as e:
    print(f"Error: {e}")