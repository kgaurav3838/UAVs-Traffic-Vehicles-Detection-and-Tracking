import cv2


def draw_rectangle(event, x, y, _, __):
    global pt1, pt2, topLeftClicked, botRightClicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeftClicked and botRightClicked:
            topLeftClicked = False
            botRightClicked = False
            pt1 = (0, 0)
            pt2 = (0, 0)

        if not topLeftClicked:
            pt1 = (x, y)
            topLeftClicked = True

        elif not botRightClicked:
            pt2 = (x, y)
            botRightClicked = True


pt1 = (0, 0)
pt2 = (0, 0)
topLeftClicked = False
botRightClicked = False

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    ret, frame = cap.read()

    if topLeftClicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if topLeftClicked and botRightClicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)

    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
