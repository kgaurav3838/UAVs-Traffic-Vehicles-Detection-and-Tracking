import cv2

tracker = cv2.TrackerBoosting_create()
cap = cv2.VideoCapture('../data/traffic.mp4')
_, frame = cap.read()
roi = cv2.selectROI(frame, False)
ret = tracker.init(frame, roi)

while True:
    _, frame = cap.read()
    success, roi = tracker.update(frame)
    (x, y, w, h) = tuple(map(int, roi))
    if success:
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
    else:
        cv2.putText(frame, "Failure to Detect Tracking!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow('BOOSTING Tracker', frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
