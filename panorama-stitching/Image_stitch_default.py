# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:42:39 2019
@author: KGaurav
"""
# Python program to explain cv2.imshow() method 

import cv2

#Read the images from your directory
left=cv2.imread('images/left1.jpg',cv2.IMREAD_COLOR)  # Left Image
right=cv2.imread('images/right1.jpg',cv2.IMREAD_COLOR)
scale_percent = 300  # percent of original size
width = int(left.shape[1] * scale_percent / 100)
height = int(left.shape[0]* scale_percent / 100)
dim = (width, height)

left=cv2.resize(left, dim, interpolation = cv2.INTER_AREA)   #ReSize image
right=cv2.resize(right, dim, interpolation = cv2.INTER_AREA) #ReSize image

images=[]
images.append(left)
images.append(right)

stitcher = cv2.createStitcher()
#stitcher = cv2.Stitcher.create()
ret,pano = stitcher.stitch(images)

if ret==cv2.STITCHER_OK:
    cv2.imshow('Panorama',pano)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Error during Stitching")

