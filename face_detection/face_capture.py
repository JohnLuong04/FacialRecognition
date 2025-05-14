from detector import Detector
import cv2 as cv

# Initializing detector
detector = Detector(
    prototxt_path="face_detection/models/deploy.prototxt", 
    model_path="face_detection/models/res10_300x300_ssd_iter_140000.caffemodel"
)

# Initializing camera
camera = cv.VideoCapture(0)
if not camera.isOpened:
    print("Camera failed to open.")
    exit()

# Using camera input to detect faces
while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Detecting faces in frame
    faces = detector.detect(frame)
    # Drawing bounding box
    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow("Face Detection", frame)

    # Checks if ESC key is pressed, and breaks if so
    if cv.waitKey(1) & 0xFF == 27:
        break

# Cleaning up
camera.release()
cv.destroyAllWindows()
