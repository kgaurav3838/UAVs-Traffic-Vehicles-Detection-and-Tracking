import cv2

video1= "R:/My Files/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"
cap = cv2.VideoCapture(video1)

width = print("Width=",int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = print("Height=",int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# recorder = cv2.VideoWriter('capture.mp4', cv2.VideoWriter_fourcc(*'VIDX'), 20, (width, height))

while True:
    _, frame = cap.read()
    cv2.imshow("Camera", frame)
    # recorder.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# recorder.release()
cap.release()
cv2.destroyAllWindows()

"""
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
"""
cap.release()
cv2.destroyAllWindows()
