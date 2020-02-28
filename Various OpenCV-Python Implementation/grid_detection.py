import cv2

img = cv2.imread('../data/flat_chessboard.png')
cv2.imshow('img', img)
cv2.waitKey(0)

found, corners = cv2.findChessboardCorners(img, (7, 7))
print(found)
print(corners)

print(cv2.drawChessboardCorners(img, (7, 7), corners, found))
cv2.imshow("img", img)
cv2.waitKey(0)

img = cv2.imread('../data/dot_grid.png')
cv2.imshow("img", img)
cv2.waitKey(0)

found, corners = cv2.findCirclesGrid(img, (10, 10), cv2.CALIB_CB_SYMMETRIC_GRID)
cv2.drawChessboardCorners(img, (10, 10), corners, found)
cv2.imshow("img", img)
cv2.waitKey(0)
