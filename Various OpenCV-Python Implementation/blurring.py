import cv2
import numpy as np

count = 0


def img_show(img2show, name="img"):
    global count
    cv2.imshow(name, img2show)
    cv2.waitKey(0)
    img2write = img2show * 255
    cv2.imwrite("Blurring - " + str(count) + ".jpg", img2write)
    count += 1


img = cv2.imread('../data/bricks.jpg').astype(np.float)/255
img_show(img)

gamma = 1/4
res = np.power(img, gamma)
img_show(res)

gamma = 2
res = np.power(img, gamma)
img_show(res)

kernel = np.ones((5, 5), dtype=np.float)/25
print(kernel)
blurWithKernel = cv2.filter2D(img, -1, kernel)
img_show(blurWithKernel, "kernel")

blurWithAvg = cv2.blur(img, (5, 5))
# 5x5 filter, each element = 1, applied filter / 25 for averaging
img_show(blurWithAvg, "avg")

blurWithGaussian = cv2.GaussianBlur(img, (5, 5), 10)
img_show(blurWithGaussian, "gaussian")

img = cv2.imread('../data/bricks.jpg')

blurWithMedian = cv2.medianBlur(img, 5)
img_show(blurWithMedian, "median")

blurWithBilateral = cv2.bilateralFilter(img, 9, 75, 75)
img_show(blurWithBilateral, "bilateral")
