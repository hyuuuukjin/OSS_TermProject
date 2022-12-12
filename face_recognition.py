import cv2
face_recognition = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def face_recog(cam):
    gray = cv2.cvtColor(cam, cv2.COLOR_BGR2GRAY)
    faces = face_recognition.detectMultiScale(gray, 1.05, 4, minSize=(200, 200))

    for (x, y, w, h) in faces:
            cv2.rectangle(cam, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # cv2.imshow('Video', frame)

    if len(faces) >= 1:
        return 1, cam, faces
    else:
        return 0, cam, faces
