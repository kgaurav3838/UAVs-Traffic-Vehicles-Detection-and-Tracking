# USAGE
# python realtime_stitching.py  # Video Stitching

# import the necessary packages
from __future__ import print_function

import datetime

import cv2
# from imutils.video import VideoStream
import numpy as np
from imagesearch.basicmotiondetector import BasicMotionDetector

# initialize the video streams and allow them to warmup
print("[INFO] starting videos...")

#video1= "R:/My Files/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"  # Work
video1 = "R:/My Files/OneDrive - IIT Kanpur/IITK OneDrive/ODAT/Tracking Videos/videos/video3.mp4"
video2 = "R:/My Files/OneDrive - IIT Kanpur/IITK OneDrive/ODAT/Tracking Videos/videos/video7.avi"

leftStream=cv2.VideoCapture(video2)

# time.sleep(2.0)
# initialize the image stitcher, motion detector, and total number of frames read
motion = BasicMotionDetector(minArea=500)
total = 0
print("[INFO] Motion detection is in progress.....")
# loop over frames from the video streams
while True:
    # grab the frames from their respective video streams
    _, left = leftStream.read()

    # resize the frames
    scale_percent = 100  # percent of original size
    width_left = int(left.shape[1] * scale_percent / 100)
    height_left = int(left.shape[0])


    dim_left = (width_left, height_left)
    # left = cv2.resize(left, dim_left, interpolation = cv2.INTER_AREA)
    #right = cv2.resize(right, dim_right, interpolation = cv2.INTER_AREA)

    # stitch the frames together to form the panorama IMPORTANT: you might have to change this line of code
    # depending on how your cameras are oriented; frames should be supplied in left-to-right order

    # no homograpy could be computed
    if left is None:
        print("[INFO] homography could not be computed")
        break

    # convert the panorama to grayscale, blur it slightly, update
    # the motion detector
    gray = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    locs = motion.update(gray)

    # only process the panorama for motion if a nice average has
    # been built up
    if total > 32 and len(locs) > 0:
        # initialize the minimum and maximum (x, y)-coordinates, respectively
        (minX, minY) = (np.inf, np.inf)
        (maxX, maxY) = (-np.inf, -np.inf)

        # loop over the locations of motion and accumulate the
        # minimum and maximum locations of the bounding boxes
        for l in locs:
            (x, y, w, h) = cv2.boundingRect(l)
            (minX, maxX) = (min(minX, x), max(maxX, x + w))
            (minY, maxY) = (min(minY, y), max(maxY, y + h))

        # draw the bounding box
        cv2.rectangle(left, (minX, minY), (maxX, maxY),
            (0, 0, 255), 3)

    # increment the total number of frames read and draw the
    # timestamp on the image
    total += 1
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(left, ts, (10, left.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # show the output images
    cv2.imshow("Left Frame", left)
   # cv2.imshow("Right Frame", right)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
# rightStream.stop()