import cv2
import numpy as np

face_cascade=cv2.CascadeClassifier('Phan05_CacBaiToanApDung/haarcascade_frontalface_default.xml')

def save_face(frame,faces):
    i=0
    for (x,y,w,h) in faces:
        i+=1
        crop=frame[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imwrite("file{}.png".format(i),crop)
    return
camera=cv2.VideoCapture(0)

while True:
    ret,img=camera.read()
    if ret:
        #chuyen img thanh sam
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.2,10,minSize=(100,100))

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("video",img)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('s'):
        save_face(img,faces)
camera.release()
cv2.destroyAllWindows()

