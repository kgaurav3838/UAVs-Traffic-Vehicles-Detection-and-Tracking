import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/horse.jpg')
img2show = img.copy()
img2show = cv2.cvtColor(img2show, cv2.COLOR_RGB2BGR)
plt.figure(1)
plt.imshow(img2show)

grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

dstHarris = cv2.cornerHarris(src=grayImg, blockSize=3, ksize=5, k=0.04)

blackBG = np.zeros(img.shape)
blackBG[dstHarris > .05 * dstHarris.max()] = [0, 0, 255]
plt.figure(2)
plt.title('cornerHarris')
plt.imshow(blackBG)

dst = cv2.goodFeaturesToTrack(grayImg, 220, 0.2, 1, blockSize=3, useHarrisDetector=True, k=0.04)
dst = np.int0(dst)

blackBG = np.zeros(img.shape)

for i in dst:
    x, y = i.ravel()
    cv2.circle(blackBG, (x, y), 3, 255, -1)

plt.figure(3)
plt.title('goodFeaturesToTrack')
plt.imshow(blackBG)
plt.show()
