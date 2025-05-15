from detector import Detector
import cv2 as cv
<<<<<<< HEAD
import os
=======
import dlib
>>>>>>> 313f89c1f13e419981d159821c465c9ff3439526

# Initializing detector
detector = Detector(
    prototxt_path="face_detection/models/deploy.prototxt", 
    model_path="face_detection/models/res10_300x300_ssd_iter_140000.caffemodel",
    predictor_path="face_detection/models/shape_predictor_68_face_landmarks.dat"
)

# Initializing camera
camera = cv.VideoCapture(0)
if not camera.isOpened():
    print("Camera failed to open.")
    exit()


dlib = dlib.shape_predictor("")

# Using camera input to detect faces
while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Detecting faces in frame
    faces, eyes = detector.detect(frame)
    # Drawing bounding box
    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for(le,re) in eyes:
        for(ex,ey) in le + re:
            cv.circle(frame, (ex,ey),2, (255,0,0), -1)
  

    # Checks if ESC key is pressed, and breaks if so
    key = cv.waitKey(1)
    if key == 27:
        break
    if key == ord('s'):
        if not os.path.exists('database/initial_face_images'):
            os.makedirs('database/initial_face_images')
        with open('initial_face_images_index.txt', 'r') as file:
            index = file.read()
            cv.imwrite(f'database/initial_face_images/face{index}.png', frame)
        with open('initial_face_images_index.txt', 'w') as file:
            file.write(str(int(index) + 1))

# Cleaning up
camera.release()
cv.destroyAllWindows()
