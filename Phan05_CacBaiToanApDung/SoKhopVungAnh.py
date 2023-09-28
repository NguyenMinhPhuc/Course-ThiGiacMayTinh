#so khớp vùng ảnh
import cv2
import numpy as np
#Đọc ảnh từ file
img_rgb=cv2.imread('Phan05_CacBaiToanApDung/images.jpg')
#thực hiện các thao tác tiền xử lý
#1.Chuyển ảnh xám
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
#Đọc ảnh cần so khớp
template=cv2.imread('Phan05_CacBaiToanApDung/template.jpg',0)

#Lấy chiều rộng (w) chiều cao của ảnh template (h)
w, h =template.shape[::-1]
#res là giá trị 0--1: càng gần  1 thì template càng giống ảnh gốc
res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)


# khai báo ngưỡng
threshold=0.9

loc=np.where(res>=threshold)
#print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,225,0),2)

#hiển thị ảnh lên
cv2.imshow('Anh phat hien',img_rgb)
cv2.waitKey(0)

