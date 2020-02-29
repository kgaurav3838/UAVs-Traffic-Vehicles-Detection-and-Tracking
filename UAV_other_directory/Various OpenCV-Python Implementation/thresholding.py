import cv2

img = cv2.imread("../data/rainbow.jpg")
cv2.imshow("Rainbow", img)
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(src=img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)  # 0 -> Black, 255 -> White
"""
THRESH_BINARY
-------------
if pixel > thresh -> pixel = max_val
else pixel = 0
"""
cv2.imshow("Thresh1", thresh1)
cv2.waitKey(0)

_, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
"""
THRESH_BINARY_INVERSE
--------------------
if pixel > thresh -> pixel = 0
else pixel = max_val
"""
cv2.imshow("Thresh2", thresh2)
cv2.waitKey(0)

_, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
"""
THRESH_TRUNC
------------
if pixel > thresh -> pixel = thresh
else pixel = pixel
"""
cv2.imshow("Thresh3", thresh3)
cv2.waitKey(0)

_, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
"""
THRESH_TOZERO
-------------
if pixel > thresh -> pixel = pixel
else pixel = 0
"""
cv2.imshow("Thresh4", thresh4)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("../data/crossword.jpg", 0)
cv2.imshow("Crossword", img)
cv2.waitKey(0)

_, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh1", thresh1)
cv2.waitKey(0)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 35)
cv2.imshow("Adaptive Thresh_Mean_C", thresh2)
cv2.waitKey(0)

thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 25)
cv2.imshow("Adaptive Thresh_Gaussian_C", thresh3)
cv2.waitKey(0)
