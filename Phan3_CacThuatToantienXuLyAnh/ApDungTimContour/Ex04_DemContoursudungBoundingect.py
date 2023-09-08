#Khai bao thu vien
import cv2
import numpy as np

#1. Doc Anh
image=cv2.imread('Phan3_CacThuatToantienXuLyAnh/ApDungTimContour/ex.jpg')

#2. Chuyen anh ve anh xam
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#_, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
#3. lam mo anh bang ham GaussianBlur
blurred=cv2.GaussianBlur(thresholded,(5,5),0)

#4. phat hien canh
edges=cv2.Canny(blurred,50,150)

#5. Tim contour trong anh
contours , _ = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


#Thiết lập diện tích giới hạn
#min_contour_area=7600
#max_contour_area=7900

#6. Đếm Contours trong ảnh
object_count=0;

for contour in contours:
    x,y,w,h=cv2.boundingRect(contour)
    #print("(x,y): (" +str(x)+(",")+str(y)+")")
    print("(w,h): (" +str(w)+(",")+str(h)+")")
    if (91<=w<=92)and (91<=h<=92):
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        object_count+=1

#7. VE contours
cv2.drawContours(image,contours,-1,(0,255,0),2)

cv2.putText(image,f'So luong: {object_count}',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)
#8. hien thi ket qua
cv2.imshow('Anh goc',image)
cv2.imshow('Anh canh',edges)

cv2.waitKey(0)
cv2.destroyAllWindow()