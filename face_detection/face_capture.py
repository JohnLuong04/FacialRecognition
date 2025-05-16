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
if not camera.isOpened():
    print("Camera failed to open.")
    exit()

# ERROR AT THIS LINE TO FIX
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
    cv.imshow("Face Detection", frame)

    for(le,re) in eyes:
        for(ex,ey) in le + re:
            cv.circle(frame, (ex,ey),2, (255,0,0), -1)

    # Checks for key presses: s for saving image, ESC for ending program
    key = cv.waitKey(1)
    if key == 27:
        break
    if key == ord('s'):
        with open('face_detection/initial_face_images_index.txt', 'r') as file:
            index = file.read()
            cv.imwrite(f'database/initial_face_images/face{index}.png', frame)
        with open('face_detection/initial_face_images_index.txt', 'w') as file:
            file.write(str(int(index) + 1))

# Cleaning up
camera.release()
cv.destroyAllWindows()
