import cv2
import matplotlib.pyplot as plt

horse = cv2.imread('../data/horse.jpg')
cv2.imshow("Horse", horse)
cv2.imwrite("Histograms.jpg", horse)
cv2.waitKey(0)

hist = cv2.calcHist([horse], [0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.savefig("Histograms - 1.jpg")
plt.show()

bricks = cv2.imread('../data/bricks.jpg')
cv2.imshow("Horse", bricks)
cv2.imwrite("Histograms - 2.jpg", bricks)
cv2.waitKey(0)

hist = cv2.calcHist([bricks], [0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(hist)
plt.savefig("Histograms - 3.jpg")
plt.show()

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv2.calcHist([bricks], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
plt.title('Bricks Image')
plt.savefig("Histograms - 4.jpg")
plt.show()

gorilla = cv2.imread('../data/gorilla.jpg')
gray_gorilla = cv2.imread('../data/gorilla.jpg', 0)

cv2.imshow("Gray Gorilla", gray_gorilla)
cv2.imwrite("Histograms - 5.jpg", gray_gorilla)
cv2.waitKey(0)
hist = cv2.calcHist([gray_gorilla], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title('Gray Gorilla Image')
plt.savefig("Histograms - 6.jpg")
plt.show()

eqGrayGorilla = cv2.equalizeHist(gray_gorilla)
hist = cv2.calcHist([eqGrayGorilla], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title('Gray Gorilla Image')
plt.savefig("Histograms - 7.jpg")
plt.show()
cv2.imshow("Gray Gorilla", eqGrayGorilla)
cv2.imwrite("Histograms - 8.jpg", eqGrayGorilla)
cv2.waitKey(0)

cv2.imshow("Gorilla", gorilla)
cv2.imwrite("Histograms - 9.jpg", gorilla)
cv2.waitKey(0)
gorilla = cv2.cvtColor(gorilla, cv2.COLOR_BGR2HSV)
gorilla[:, :, 2] = cv2.equalizeHist(gorilla[:, :, 2])
gorilla = cv2.cvtColor(gorilla, cv2.COLOR_HSV2BGR)
cv2.imshow("Gorilla", gorilla)
cv2.imwrite("Histograms - 10.jpg", gorilla)
cv2.waitKey(0)
