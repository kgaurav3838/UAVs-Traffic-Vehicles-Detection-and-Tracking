import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/pennies.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
plt.imshow(img)
plt.show()

blurred = cv2.medianBlur(img, 35)
plt.imshow(blurred)
plt.show()

gray = cv2.cvtColor(blurred, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()

_, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)
plt.imshow(thresh, cmap='gray')
plt.show()

_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(img, contours, i, (0, 0, 255), 10)

plt.imshow(img)
plt.show()

distTransform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
plt.imshow(distTransform, cmap='gray')
plt.show()

_, fg = cv2.threshold(distTransform, 0.7 * distTransform.max(), 255, 0)
plt.imshow(fg, cmap='gray')
plt.show()

fg = np.uint8(fg)
unknown = cv2.subtract(thresh, fg)
plt.imshow(unknown, cmap='gray')
plt.show()

_, markers = cv2.connectedComponents(fg)
markers = markers+1
markers[unknown == 255] = 0
plt.imshow(markers, cmap='gray')
plt.show()

markers = cv2.watershed(img, markers)
plt.imshow(markers)
plt.show()

img = cv2.imread('../data/pennies.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

_, contours, hierarchy = cv2.findContours(markers, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(img, contours, i, (255, 0, 0), 10)

plt.imshow(img)
plt.show()
