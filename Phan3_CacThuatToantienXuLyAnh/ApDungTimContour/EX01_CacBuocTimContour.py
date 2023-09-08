#Khai bao thu vien
import cv2
import numpy as np

#1. Doc Anh
image=cv2.imread('Phan3_CacThuatToantienXuLyAnh/ApDungTimContour/sample.png')

#2. Chuyen anh ve anh xam
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#3. lam mo anh bang ham GaussianBlur
blurred=cv2.GaussianBlur(gray,(5,5),0)

#4. phat hien canh
edges=cv2.Canny(blurred,50,150)

#5. Tim contour trong anh
contours , _ = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#6. VE contours
cv2.drawContours(image,contours,-1,(0,255,0),2)

#7. hien thi ket qua
cv2.imshow('Anh goc',image)
cv2.imshow('Anh canh',edges)

cv2.waitKey(0)
cv2.destroyAllWindow()