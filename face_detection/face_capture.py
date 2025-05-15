from detector import Detector
import cv2 as cv
import dlib

# Initializing detector
detector = Detector(
    prototxt_path="face_detection/models/deploy.prototxt", 
    model_path="face_detection/models/res10_300x300_ssd_iter_140000.caffemodel",
    predictor_path="face_detection/models/shape_predictor_68_face_landmarks.dat"
)

# Initializing camera
camera = cv.VideoCapture(0)
if not camera.isOpened:
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
    if cv.waitKey(1) & 0xFF == 27:
        break

# Cleaning up
camera.release()
cv.destroyAllWindows()
