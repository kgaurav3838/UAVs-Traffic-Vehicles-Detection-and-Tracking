import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/rabbits.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
eye = gray[395:435, 310:365]
img2show = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
plt.imshow(img2show)
plt.show()
plt.imshow(eye, cmap='gray')
plt.show()

methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF_NORMED']
h, w = eye.shape

for method in methods:
    detected = img.copy()
    res = cv2.matchTemplate(gray, eye, eval(method))
    plt.imshow(res)
    plt.title(method)
    plt.show()

    if eval(method) in [cv2.TM_SQDIFF_NORMED]:
        threshold = 0.27
        loc = np.where(res <= threshold)
        cv2.rectangle(detected, (loc[1][0], loc[0][0]), (loc[1][0] + w, loc[0][0] + h), (0, 0, 255), 2)
        cv2.rectangle(detected, (loc[1][-1], loc[0][-1]), (loc[1][-1] + w, loc[0][-1] + h), (255, 0, 0), 2)
        detected = cv2.cvtColor(detected, cv2.COLOR_RGB2BGR)
        plt.imshow(detected)
        plt.title(method)
        plt.show()
    else:
        threshold = 0.9
        loc = np.where(res >= threshold)
        cv2.rectangle(detected, (loc[1][0], loc[0][0]), (loc[1][0] + w, loc[0][0] + h), (0, 0, 255), 2)
        cv2.rectangle(detected, (loc[1][-1], loc[0][-1]), (loc[1][-1] + w, loc[0][-1] + h), (255, 0, 0), 2)
        detected = cv2.cvtColor(detected, cv2.COLOR_RGB2BGR)
        plt.imshow(detected)
        plt.title(method)
        plt.show()
