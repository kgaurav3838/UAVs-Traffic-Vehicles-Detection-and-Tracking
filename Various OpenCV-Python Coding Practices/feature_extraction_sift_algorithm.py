import cv2

img = cv2.imread('../data/pisa.jpg')
copyImg = img.copy()
richImg = img.copy()
cv2.imshow('IMG', img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

cv2.drawKeypoints(gray, kp, outImage=copyImg)
cv2.imshow('SIFT without Flag', copyImg)
cv2.waitKey(0)

cv2.drawKeypoints(gray, kp, outImage=richImg, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT with Flag', richImg)
cv2.imwrite('')
cv2.waitKey(0)
