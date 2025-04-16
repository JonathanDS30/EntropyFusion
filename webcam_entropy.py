import hashlib
import cv2

def capture_webcam_entropy():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return ""
    # On prend les données brutes de la photo
    return hashlib.sha256(frame.tobytes()).hexdigest()
