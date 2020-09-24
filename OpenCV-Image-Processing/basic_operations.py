import cv2
import matplotlib.pyplot as plt

img = cv2.imread("puppy.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)

dims = img.shape
width = dims[0]
height = dims[1]

img = cv2.resize(img, (int(width/2), int(height/2)))
cv2.imshow("New Image", img)
cv2.waitKey(0)

img = cv2.resize(img, (0, 0), img, .5, .5)
cv2.imshow("New Image", img)
cv2.waitKey(0)

img = cv2.flip(img, 0)
cv2.imshow("Flipped Image", img)
cv2.waitKey(0)

cv2.imwrite("new_flipped_puppy.jpg", img)
cv2.destroyAllWindows()

fig = plt.figure(figsize=(2,2))
ax = fig.add_subplot(111)
ax.imshow(img)
plt.show()
