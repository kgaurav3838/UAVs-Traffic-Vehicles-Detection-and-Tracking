import cv2

img = cv2.imread('../data/pisa.jpg')
copyImg = img.copy()
cv2.imshow('IMG', img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
kp = orb.detect(gray, None)

cv2.drawKeypoints(gray, kp, outImage=copyImg, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('ORB', copyImg)
cv2.waitKey(0)
