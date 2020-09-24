import cv2

img = cv2.imread('../data/rabbit.jpg')
cv2.imshow('img', img)
cv2.imwrite('Median Blur, Median Filter.jpg', img)
cv2.waitKey(0)

median = cv2.medianBlur(img, ksize=5)
cv2.imshow('median', median)
cv2.imwrite('Median Blur, Median Filter - 2.jpg', median)
cv2.waitKey(0)

median = cv2.medianBlur(img, ksize=7)
cv2.imshow('median', median)
cv2.imwrite('Median Blur, Median Filter - 3.jpg', median)
cv2.waitKey(0)

median = cv2.medianBlur(img, ksize=9)
cv2.imshow('median', median)
cv2.imwrite('Median Blur, Median Filter - 4.jpg', median)
cv2.waitKey(0)

median = cv2.medianBlur(img, ksize=11)
cv2.imshow('median', median)
cv2.imwrite('Median Blur, Median Filter - 5.jpg', median)
cv2.waitKey(0)
