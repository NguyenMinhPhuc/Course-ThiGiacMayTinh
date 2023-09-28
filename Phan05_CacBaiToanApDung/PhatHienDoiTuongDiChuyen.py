import cv2
import numpy as np

cap=cv2.VideoCapture(0)
frame_width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#khai bao chuan video xuat ra: Xvid
fourcc=cv2.VideoWriter_fourcc('X','V','I','D')

out =cv2.VideoWriter('outvideo.avi',fourcc,5.0,(1280,720))

ret,frame1=cap.read()

ret,frame2=cap.read()
print(frame1.shape)
while True:
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)

    contoures,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contoures:
        (x,y,w,h)=cv2.boundingRect(contour)
        #chỉ xét các contour có diện tích >900
        if cv2.contourArea(contour)<9000:
            continue
        #vẽ khung trên fram1 là vị trị đối tượng phát hiện được
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        #ghi chú lên frame1
        cv2.putText(frame1,"Trang thai: {}".format('phat hien'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    image=cv2.resize(frame1,(1280,720))
    out.write(image)
    cv2.imshow('video',frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
out.release()



