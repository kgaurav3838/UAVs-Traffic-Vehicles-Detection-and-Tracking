import cv2
import numpy as np

img = cv2.imread('../data/sammy.jpg')
cv2.imshow("Dog", img)
cv2.imwrite("Edge Detection.jpg", img)
cv2.waitKey(0)

canny1 = cv2.Canny(img, 127, 127)
cv2.imshow("Canny1", canny1)
cv2.imwrite("Edge Detection - 2.jpg", canny1)
cv2.waitKey(0)

blurredImg = cv2.blur(img, ksize=(5, 5))
canny2 = cv2.Canny(blurredImg, 127, 127)
cv2.imshow("Canny2", canny2)
cv2.imwrite("Edge Detection - 3.jpg", canny2)
cv2.waitKey(0)

med_val = np.median(blurredImg)
lower = int(max(0, .7 * med_val))
upper = int(min(255, 1.3 * med_val))
canny3 = cv2.Canny(blurredImg, lower, upper + 50)
cv2.imshow("Canny3", canny3)
cv2.imwrite("Edge Detection - 4.jpg", canny3)
cv2.waitKey(0)
