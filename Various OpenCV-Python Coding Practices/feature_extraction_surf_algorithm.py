import cv2

img = cv2.imread('../data/pisa.jpg')
copyImg = img.copy()
richImg = img.copy()
cv2.imshow('IMG', img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create(2000)
kp = surf.detect(gray, None)

cv2.drawKeypoints(gray, kp, outImage=copyImg)
cv2.imshow('SURF Keypoints', copyImg)
cv2.waitKey(0)

cv2.drawKeypoints(gray, kp, outImage=richImg, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF Keypoints with Orientation', richImg)
cv2.waitKey(0)

richImg = img.copy()
surf.setUpright(True)
kp = surf.detect(gray, None)

cv2.drawKeypoints(gray, kp, outImage=richImg, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF Keypoints without Orientation', richImg)
cv2.waitKey(0)
