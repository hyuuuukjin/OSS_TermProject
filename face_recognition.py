import cv2

def face_recognition(cam):
    faces = face_recognition.detectMultiScale(gray, 1.05, 4, minSize=(200, 200))

    for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('Video', frame)

    if faces >= 1:
        return 1
    else:
        return 0
