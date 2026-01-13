import cv2
import face_recognition
import numpy as np
import pickle

def parse_image(file_bytes):
    nparr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None: raise ValueError('Invalid image')
    return img

def map_face(img):
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    if not boxes: return None
    return face_recognition.face_encodings(rgb, boxes)[0]

def to_bytes(encoding):
    return pickle.dumps(encoding)

def from_bytes(bts):
    return pickle.loads(bts) if bts else None

def identify(known, target, tolerance=0.6):
    matches = face_recognition.compare_faces(known, target, tolerance=tolerance)
    if True in matches:
        return matches.index(True)
    return -1
