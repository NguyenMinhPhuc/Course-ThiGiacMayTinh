from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours

import numpy as np
import argparse
import imutils
import cv2

def read_and_preproces(filename,canny_low=50,canny_hight=100,blur_kernel=9,d_e_kernel=3):
    #doc anh 
    image=cv2.imread(filename)
    #chuyen ve anh xam
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #lam mo anh
    gray=cv2.GaussianBlur(gray,(blur_kernel,blur_kernel),0)
    #tim canny
    edged=cv2.Canny(gray,canny_low,canny_hight)
    edged=cv2.dilate(edged,(d_e_kernel,d_e_kernel),iterations=1)
    edged=cv2.erode(edged,(d_e_kernel,d_e_kernel),iterations=1)
    return image,edged

image,edged=read_and_preproces('Images.jpg')
cv2.imshow('edged',edged)
cv2.waitKey()
#Lay trung binh cua diem anh
def midpoint(ptA,ptB):
    return (ptA[0]+ptB[0])/2,(ptA[1]+ptB[1])/2
#   
def get_distance_in_pixel(orig,c):
    box=cv2.minAreaRect(c)
    box=cv2.boxPoints(box)
    box=np.array(box,dtype="int")
    
    #sap xep cac diem theo trinh tu
    box=perspective.order_points(box)
    
    cv2.drawContours(orig,[box.astype("int")],-1,(0,255,0),2)
    
    #tinh toan trung diem cua cac canh
    tl,tr,br,bl=box
    
    (tltrX,tltrY)=midpoint(tl,tr)
    (blbrX,blbrY)=midpoint(bl,br)
    (tlblX,tlblY)=midpoint(tl,bl)
    (trbrX,trbrY)=midpoint(tr,br)
    
    #tinh do dai 2 chieu
    dc_W=dist.euclidean((tltrX,tltrY),(blbrX,blbrY))
    dc_H=dist.euclidean((tlblX,tlblY),(trbrX,trbrY))

    return dc_W,dc_H,tltrX,tltrY,trbrX,trbrY
ref_width=200
# viet tim doi tuong
def find_object_in_pix(orig,edge,area_threashold=3000):
    #tim contours trong anh
    cnts=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    
    (cnts,_)=contours.sort_contours(cnts)
    P=None
    #duyet tung contours
    for c in cnts:
        if cv2.contourArea(c)<area_threashold:
            continue
        
        #tinh toan dc_W,dc_H,trung diem
        dc_W,dc_H,tltrX,tltrY,trbrX,trbrY=get_distance_in_pixel(orig,c)
        
        #xac dinh dong xu
        if P is None:
            #cap nhat lai 
            P=ref_width/dc_H
            dr_W=ref_width
            dr_H=ref_width
        else:
            dr_W=dc_W*P
            dr_H=dc_H*P
        cv2.putText(orig,"{:.1f} mm".format(dr_H),(int(tltrX-15),int(tltrY-10)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
        cv2.putText(orig,"{:.1f} mm".format(dr_W),(int(trbrX+10),int(trbrY)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    return orig

image=find_object_in_pix(image,edged)
cv2.imshow("orig",image)
cv2.waitKey()
cv2.destroyAllWindows()
