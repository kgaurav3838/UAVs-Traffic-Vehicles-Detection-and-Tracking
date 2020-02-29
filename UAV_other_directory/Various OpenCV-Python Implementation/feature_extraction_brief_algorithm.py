import cv2

img = cv2.imread('../data/pisa.jpg')
copyImg = img.copy()
cv2.imshow('IMG', img)
cv2.waitKey(0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp = fast.detect(gray, None)
kp, descriptors = brief.compute(gray, kp)
cv2.drawKeypoints(gray, kp, copyImg, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('FAST and BRIEF', copyImg)
cv2.waitKey(0)
