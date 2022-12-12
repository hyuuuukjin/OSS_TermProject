import cv2
import time
import face_recognition

def check_face(frame, output):
    val = face_recognition.face_recog(frame, output)
    return val[0], val[1]
