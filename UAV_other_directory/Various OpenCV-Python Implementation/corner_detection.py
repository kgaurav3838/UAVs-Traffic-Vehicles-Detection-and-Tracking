import cv2

img = cv2.imread('../data/flat_chessboard.png')
cv2.imshow("Chess", img)
cv2.waitKey(0)

grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
dst = cv2.cornerHarris(src=grayImg, blockSize=2, ksize=3, k=0.04)
dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow("Chess", img)
cv2.waitKey(0)
