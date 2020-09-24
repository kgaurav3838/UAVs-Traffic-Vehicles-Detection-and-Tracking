import cv2
import numpy as np

img = cv2.imread('../data/internal_external.png', 0)
cv2.imshow('img', img)
cv2.waitKey(0)

_, contours, hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
print(hierarchy)

contours1 = np.zeros(img.shape)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(contours1, contours, i, 255, -1)

cv2.imshow("img", contours1)
cv2.waitKey(0)

contours2 = np.zeros(img.shape)
for i in range(len(contours)):
    if hierarchy[0][i][3] == 0:
        cv2.drawContours(contours2, contours, i, 255, -1)

cv2.imshow("img", contours2)
cv2.waitKey(0)

contours3 = np.zeros(img.shape)
for i in range(len(contours)):
    if hierarchy[0][i][3] == 4:
        cv2.drawContours(contours3, contours, i, 255, -1)

cv2.imshow("img", contours3)
cv2.waitKey(0)
