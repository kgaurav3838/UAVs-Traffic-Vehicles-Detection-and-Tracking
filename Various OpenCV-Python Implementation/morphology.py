import cv2
import numpy as np

img = np.zeros((600, 600))
cv2.putText(img, "JAN", (150, 350), cv2.FONT_HERSHEY_SIMPLEX, 5, 255, 25)
cv2.imshow("Black background", img)
cv2.waitKey(0)
print(img)

kernel = np.ones((5, 5))
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erosion - 1 Iteration", erosion)
cv2.waitKey(0)

erosion = cv2.erode(img, kernel, iterations=5)
cv2.imshow("Erosion - 5 Iteration", erosion)
cv2.waitKey(0)

dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilation - 1 Iteration", dilation)
cv2.waitKey(0)

dilation = cv2.dilate(img, kernel, iterations=5)
cv2.imshow("Dilation - 5 Iteration", dilation)
cv2.waitKey(0)

whiteNoise = np.random.randint(low=-1, high=2, size=(600, 600))
whiteNoise *= 255
whiteNoisedImg = img + whiteNoise
whiteNoisedImg[whiteNoisedImg == -255] = 0
cv2.imshow("White Noised Img", whiteNoisedImg)
print(whiteNoisedImg)
cv2.waitKey(0)

kernel = np.ones((2, 2))
opening = cv2.morphologyEx(whiteNoisedImg, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey(0)

closing = cv2.morphologyEx(whiteNoisedImg, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)
