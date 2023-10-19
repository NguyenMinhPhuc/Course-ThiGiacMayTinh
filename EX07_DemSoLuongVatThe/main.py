import cv2

path='images/black-dot1.jpg'
path2='images/white-dot.png'
path1='images/download.jpg'
image=cv2.imread(path1,1)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#blurred=cv2.GaussianBlur(gray,(5,5),0)

th,threshed=cv2.threshold(gray,127,225,cv2.THRESH_BINARY)

cnts=cv2.findContours(threshed,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]

s1=200
s2=3000
xcnts=[]
for cnt in cnts:
    print("area:{}".format(cv2.contourArea(cnt)))
    if s1<=cv2.contourArea(cnt)<=s2:
        xcnts.append(cnt)
        cv2.drawContours(image, cnt, -1, (0, 255, 0), 1)
#in so luong dem duoc
print("\n So luong dau cham : {}".format(len(xcnts)))
#1. ve contour le anh goc
#2. hien thi anh goc len
cv2.imshow('anh go',image)
cv2.imshow('anh nguong',threshed)

cv2.waitKey(0)
cv2.destroyAllWindows()