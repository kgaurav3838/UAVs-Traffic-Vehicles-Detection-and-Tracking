import cv2
import matplotlib.pyplot as plt

dogImg = cv2.imread('../data/sammy.jpg')
faceImg = cv2.imread('../data/sammy_face.jpg')

dogImg = cv2.cvtColor(dogImg, cv2.COLOR_RGB2BGR)
faceImg = cv2.cvtColor(faceImg, cv2.COLOR_RGB2BGR)

plt.title("Dog image")
plt.imshow(dogImg)
plt.show()

plt.title("Face of the dog")
plt.imshow(faceImg)
plt.show()

height, width, _ = faceImg.shape
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:

    full = dogImg.copy()

    res = cv2.matchTemplate(full, faceImg, eval(m))
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)

    if eval(m) in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        topLeft = minLoc
    else:
        topLeft = maxLoc

    bottomRight = (topLeft[0] + width, topLeft[1] + height)
    cv2.rectangle(full, topLeft, bottomRight, (0, 0, 255), 5)

    plt.subplot(121)
    plt.imshow(res)
    plt.title('Result of Template Matching')

    plt.subplot(122)
    plt.imshow(full)
    plt.title('Detected Point')
    plt.suptitle(m)
    plt.show()
