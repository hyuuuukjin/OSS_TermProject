#202235134 MinSeok Choi
import cv2
import time
import lim_determine
# import FaceMesh

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
            # frame1 = FaceMesh.Pritreatment(frame)
            check += lim_determine.check_face(frame)
            cv2.imshow("test", frame)
            if cv2.waitKey(1) > 0:
                break
        if curframe == 10:
            if check >= 7:
                print("face detected")
            else:
                print("No face")
            curframe = 0
            check = 0

    webcam.release()
    cv2.destroyAllWindows()