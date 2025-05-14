from face_detection import Detector
import cv2 as cv

detector = Detector(
    "face_detection/models/deploy.prototxt", 
    "face_detection/models/res10_300x300_ssd_iter_140000.caffemodel"
)

camera = cv.VideoCapture(0)

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

camera.release()
cv.destroyAllWindows()