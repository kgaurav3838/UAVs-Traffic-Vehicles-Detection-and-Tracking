# USAGE
# python realtime_stitching.py  # Video Stitching

# import the necessary packages
from __future__ import print_function

# from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

# initialize the video streams and allow them to warmup
print("[INFO] starting videos...")

video1= "R:/My Files/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"  # Work
video2= "R:/My Files//OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 2/DJI_0152.MOV"

leftStream=cv2.VideoCapture(video1)
rightStream = cv2.VideoCapture(video2)
width = print("Width=",int(leftStream.get(cv2.CAP_PROP_FRAME_WIDTH)))
height = print("Height=",int(leftStream.get(cv2.CAP_PROP_FRAME_HEIGHT)))
time.sleep(2.0)
total = 0
print("[INFO] Video Stitching is in progress...")
# loop over frames from the video streams
while True:
    _, left = leftStream.read()
    #right = rightStream.read()

    scale_percent = 60  # percent of original size
    width_left = int(left.shape[1] * scale_percent / 100)
    height_left = int(left.shape[0] * scale_percent / 100)
    dim_left = (width_left, height_left)
    left = cv2.resize(left, dim_left, interpolation = cv2.INTER_AREA)


    # increment the total number of frames read and draw the timestamp on the image
    total += 1
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(left, ts, (10, left.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("video1", left)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
#rightStream.stop()