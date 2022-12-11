#202235134 MinSeok Choi

import cv2
import time

def webcam_main():
    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Could not open webcam")
        exit()

    prev_time = 0
    FPS = 10

    while 1:
        ret, frame = webcam.read()
        current_time = time.time() - prev_time
        if (ret is True) and (current_time > 1. / FPS):
            prev_time = time.time()
            frame = cv2.flip(frame, 1)
            # cv2.imshow('VideoCapture', frame)
            if cv2.waitKey(1) > 0:
                break

    webcam.release()
    cv2.destroyAllWindows()

webcam_main()