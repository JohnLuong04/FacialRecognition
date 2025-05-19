from deepface import DeepFace
import cv2 as cv
import numpy as np
import os

input_folder = "database/initial_face_images"
output_folder = "database/embedded_face_vectors"
os.makedirs(output_folder, exist_ok=True)

for image in os.listdir(input_folder):
    image_path = os.path.join(input_folder, image)
    img = cv.imread(image_path)

    if img is None:
        print(f"Failed to load {image_path}")
        continue
    try:
        embedding = DeepFace.represent(img_path=image_path, model_name='Facenet', enforce_detection=False)[0]["embedding"]
        name = os.path.splitext(image)[0]
        np.save(os.path.join(output_folder, f"{name}.npy"), embedding)
    except Exception as e:
        print(f"Error processing {image}: {e}")
