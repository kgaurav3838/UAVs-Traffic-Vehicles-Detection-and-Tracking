import cv2

img = cv2.imread('../data/barney.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
frontalfaceHaarCascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
frontalRect = frontalfaceHaarCascade.detectMultiScale(gray)
imgForFace = img.copy()

for (x, y, w, h) in frontalRect:
    cv2.rectangle(imgForFace, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('img', imgForFace)
cv2.waitKey(0)

eyeHaarCascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')
eyeRect = eyeHaarCascade.detectMultiScale(gray)
imgForEyes = img.copy()

for (x, y, w, h) in eyeRect:
    cv2.rectangle(imgForEyes, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow('img', imgForEyes)
cv2.waitKey(0)
cv2.destroyAllWindows()
