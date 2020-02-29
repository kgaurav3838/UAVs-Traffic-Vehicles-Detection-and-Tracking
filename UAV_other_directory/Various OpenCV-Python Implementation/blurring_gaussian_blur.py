import cv2

img = cv2.imread('../data/rabbit.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=3)
cv2.imshow('3,3,3', gauss)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=3)
cv2.imshow('5,5,3', gauss)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(7, 7), sigmaX=3)
cv2.imshow('7,7,3', gauss)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(9, 9), sigmaX=3)
cv2.imshow('9,9,3', gauss)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=1)
cv2.imshow('5,5,1', gauss)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=3)
cv2.imshow('5,5,3', gauss)
cv2.waitKey(0)

gauss = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=10)
cv2.imshow('5,5,10', gauss)
cv2.waitKey(0)
