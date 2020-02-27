import cv2
import numpy as np
from matplotlib import cm

img = cv2.imread('../data/road_image.jpg')
copyImg = img.copy()
cv2.imshow('road img', img)
cv2.waitKey(0)
cv2.destroyWindow('road img')


def create_rgb(j):
    x = np.array(cm.tab10(j))[:3]*255
    return tuple(x)


colors = []
for i in range(10):
    colors.append(create_rgb(i))

marker_image = np.zeros(img.shape[:2], dtype=np.int32)
segments = np.zeros(img.shape, dtype=np.uint8)

n_markers = 10
current_marker = 1
marks_updated = False


def mouse_callback(event, x, y, _, __):
    global marks_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image, (x, y), 10, current_marker, -1)
        cv2.circle(copyImg, (x, y), 10, colors[current_marker], -1)
        marks_updated = True


cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image', mouse_callback)

while True:
    cv2.imshow('WaterShed Segments', segments)
    cv2.imshow('Road Image', copyImg)

    k = cv2.waitKey(1)

    if k == 27:
        break

    elif k == ord('c'):
        road_copy = img.copy()
        marker_image = np.zeros(img.shape[0:2], dtype=np.int32)
        segments = np.zeros(img.shape, dtype=np.uint8)

    elif k > 0 and chr(k).isdigit():
        current_marker = int(chr(k))

    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(img, marker_image_copy)
        segments = np.zeros(img.shape, dtype=np.uint8)

        for color_ind in range(n_markers):
            segments[marker_image_copy == color_ind] = colors[color_ind]

        marks_updated = False

cv2.destroyAllWindows()
