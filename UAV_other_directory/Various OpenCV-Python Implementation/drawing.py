import cv2
import matplotlib.pyplot as plt
import numpy as np

blankImg = np.zeros((512, 512, 3), dtype=np.int16)
plt.imshow(blankImg)
plt.show()

cv2.rectangle(blankImg, pt1=(12, 25), pt2=(150, 400), color=(0, 255, 0), thickness=5)
plt.imshow(blankImg)
plt.show()

cv2.rectangle(blankImg, pt1=(50, 50), pt2=(100, 100), color=(255, 0, 0), thickness=5)
cv2.circle(blankImg, center=(200, 200), radius=25, color=(0, 0, 255), thickness=5)
cv2.circle(blankImg, center=(300, 360), radius=40, color=(0, 0, 255), thickness=-1)
plt.imshow(blankImg)
plt.show()

cv2.line(blankImg, pt1=(0, 0), pt2=(450, 450), color=(125, 125, 0), thickness=2)
plt.imshow(blankImg)
plt.show()

blankImg = np.zeros((512, 512, 3), dtype=np.int16)
plt.imshow(blankImg)
plt.show()

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blankImg, text='Hello blankImg', org=(10, 400), fontFace=font, fontScale=2,
            color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
plt.imshow(blankImg)
plt.show()

points = np.array([[50, 150], [100, 100], [200, 150], [100, 200]], dtype=np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(blankImg, [points], isClosed=True, color=(0, 255, 0), thickness=5)
plt.imshow(blankImg)
plt.show()
