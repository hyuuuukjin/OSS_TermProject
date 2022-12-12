import cv2
import time
import face_recognition

def check_face(frame):
    val = face_recognition.face_recog(frame)
    return val[0]