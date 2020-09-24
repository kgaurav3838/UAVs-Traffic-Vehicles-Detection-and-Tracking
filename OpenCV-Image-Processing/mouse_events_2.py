import cv2
import numpy as np

img = np.zeros((512, 512, 3))
draw = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flag, params):
    global draw, ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.rectangle(img, (ix, ix), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.rectangle(img, (ix, ix), (x, y), (0, 255, 0), -1)


cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', draw_rectangle)

while True:

    cv2.imshow('Paint', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.imwrite("asd.jpg", img)
cv2.destroyAllWindows()
