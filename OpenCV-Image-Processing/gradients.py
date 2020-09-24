import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img2show):
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img2show, cmap='gray')
    plt.show()


img = cv2.imread('../data/sudoku.jpg', 0)
display_img(img)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
laplacian = cv2.Laplacian(img, cv2.CV_64F)

display_img(sobelX)
display_img(sobelY)
display_img(laplacian)

blended = cv2.addWeighted(src1=sobelX, alpha=0.5, src2=sobelY, beta=0.5, gamma=0)
display_img(blended)

kernel = np.ones((4, 4), np.uint8)
gradient = cv2.morphologyEx(blended, cv2.MORPH_GRADIENT, kernel)
display_img(gradient)

_, th = cv2.threshold(blended, 100, 255, cv2.THRESH_BINARY_INV)
display_img(th)

gradient = cv2.morphologyEx(laplacian, cv2.MORPH_GRADIENT, kernel)
display_img(gradient)
