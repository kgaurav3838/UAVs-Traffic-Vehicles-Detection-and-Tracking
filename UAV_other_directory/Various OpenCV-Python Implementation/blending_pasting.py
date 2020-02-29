import cv2
import numpy as np

img = cv2.imread("data/puppy.jpg")
img2 = cv2.imread("data/no_copy.png")

imgWidth, imgHeight, _ = img.shape
img2Width, img2Height, _ = img2.shape
img = cv2.resize(img, (int(imgHeight/2), int(imgWidth/2)))
img2 = cv2.resize(img2, (int(img2Height/8), int(img2Width/8)))
img2Width, img2Height, _ = img2.shape

cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.imshow("Img2", img2)
cv2.waitKey(0)

dogFace = img[60:60+img2Height, 180:180+img2Width]
cv2.imshow("dogFace", dogFace)
cv2.waitKey(0)

img2_grayscale = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
mask_inv = cv2.bitwise_not(img2_grayscale)
cv2.imshow("mask_inv", mask_inv)
cv2.waitKey(0)

white_background = np.full(img2.shape, 255, dtype=np.uint8)
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
print(bk.shape)
fg = cv2.bitwise_or(img2, img2, mask=mask_inv)
cv2.imshow("fg", fg)
cv2.waitKey(0)

dogFace = cv2.resize(dogFace, (160, 160))
fg = cv2.resize(fg, (160, 160))
final_roi = cv2.bitwise_or(dogFace, fg)
img[60:60+img2Height+1, 180:180+img2Width] = final_roi
cv2.imshow("img", img)
cv2.waitKey(0)
