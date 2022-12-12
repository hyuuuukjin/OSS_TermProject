#202235134 MinSeok Choi
import cv2
import time
import lim_determine
import FaceMesh

def webcam_main():
    check = 0
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        print("Could not open webcam")
        exit()
    prev_time = 0
    FPS = 2
    curframe = 0
    while 1:
        ret, frame = webcam.read()
        current_time = time.time() - prev_time
        if (ret is True) and (current_time > 1. / FPS):
            curframe += 1
            prev_time = time.time()
            frame = cv2.flip(frame, 1)
            output = FaceMesh.Pritreatment(frame)
            val = lim_determine.check_face(frame, output)
            check += val[0]
            output = val[1]
            # cv2.imshow("test", output)
            if cv2.waitKey(1) > 0:
                break
        if curframe == 10:
            if check >= 7:
                print("Attending Class.")
            else:
                print("NOT Attending Class.")
            curframe = 0
            check = 0

    webcam.release()
    cv2.destroyAllWindows()
