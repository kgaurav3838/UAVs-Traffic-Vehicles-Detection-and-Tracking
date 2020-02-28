import cv2
import time

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
recorder = cv2.VideoWriter('capture.mp4', cv2.VideoWriter_fourcc(*'VIDX'), 20, (width, height))

while True:
    _, frame = cap.read()
    cv2.imshow("Camera", frame)
    recorder.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

recorder.release()
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture('capture.mp4')

if not cap.isOpened():
    print("Error")

while True:
    ret, frame = cap.read()

    if ret:
        time.sleep(1/20)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
