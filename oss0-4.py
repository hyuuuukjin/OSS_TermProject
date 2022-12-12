import cv2
import time

def check_face():
    for i in range(10):
        x=face_recognition(cam)
        sum+=x
        time.sleep(1)

    if sum>7:
        print("Face recognition success")
    else:
        print("Face recognition failed")