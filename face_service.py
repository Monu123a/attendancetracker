import face_recognition
import cv2
import numpy as np
import pickle

def load_image(file_bytes):
    nparr = np.frombuffer(file_bytes, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

def get_face_encoding(img):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb_img)
    if not boxes: return None
    return face_recognition.face_encodings(rgb_img, boxes)[0]

def serialize_encoding(encoding):
    return pickle.dumps(encoding)

def deserialize_encoding(encoding_bytes):
    if not encoding_bytes: return None
    return pickle.loads(encoding_bytes)

def match_face(known_encodings, face_encoding_to_check, tolerance=0.6):
    matches = face_recognition.compare_faces(known_encodings, face_encoding_to_check, tolerance=tolerance)
    if True in matches:
        return matches.index(True)
    return -1
