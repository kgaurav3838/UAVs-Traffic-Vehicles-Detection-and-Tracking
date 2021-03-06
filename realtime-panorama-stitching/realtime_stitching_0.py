# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 17:42:39 2020
@author: KGaurav
"""
# python realtime_stitching.py  # Video Stitching
# import the necessary packages
from __future__ import print_function

import datetime
import time

import cv2
import imutils
import numpy as np
from imagesearch.basicmotiondetector import BasicMotionDetector
from imagesearch.panorama import Stitcher
from imutils.video import VideoStream

# initialize the video streams and allow them to warmup
print("[INFO] starting videos...")

#video1= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-2/2.mp4"   # Home
#video2= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-2/3.mp4"   # Home
#video1= "R:/My Files/OneDrive - IIT Kanpur\IITK OneDrive\Videos/video-data-2/2.mp4"   # Work
#video2= "R:/My Files/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-2/3.mp4"  # Work
#video1= "E:/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"  # Home
#video2= "E:/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 2/DJI_0152.MOV"  # Home
#video1= "R:/My Files/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"  # Work
#video2= "R:/My Files//OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 2/DJI_0152.MOV"
#video1= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-3/first.mp4"
#video2= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-3/third.mp4"
video1 = "R:/My Files/OneDrive - IIT Kanpur/Video Data/DJI 19 march GT Road/First Testing/2nd Drone/DJI_0001.MP4"
video2 = "R:/My Files/OneDrive - IIT Kanpur/Video Data/DJI 19 march GT Road/First Testing/3nd Drone/DJI_0001.MP4"
leftStream = VideoStream(video1).start()
rightStream = VideoStream(video2).start()

time.sleep(2.0)
# initialize the image stitcher, motion detector, and total number of frames read
stitcher = Stitcher()
motion = BasicMotionDetector(minArea=500)
total = 0
print("[INFO] Video Stitching is in progress...")

# loop over frames from the video streams
while True:
    # grab the frames from their respective video streams
    left = leftStream.read()
    right = rightStream.read()

    # resize the frames while keeping height unchanged
    left = imutils.resize(left, width=400)
    right = imutils.resize(right, width=400)

    # stitch the frames together to form the panorama IMPORTANT: you might have to change this line of code
    # depending on how your cameras are oriented; frames should be supplied in left-to-right order
    result = stitcher.stitch([left, right])

    # no homograpy could be computed
    if result is None:
        print("[INFO] homography could not be computed")
        break

    # convert the panorama to grayscale, blur it slightly, update
    # the motion detector
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    locs = motion.update(gray)

    # only process the panorama for motion if a nice average has
    # been built up
    if total > 32 and len(locs) > 0:
        # initialize the minimum and maximum (x, y)-coordinates,
        # respectively
        (minX, minY) = (np.inf, np.inf)
        (maxX, maxY) = (-np.inf, -np.inf)

        # loop over the locations of motion and accumulate the
        # minimum and maximum locations of the bounding boxes
        for l in locs:
            (x, y, w, h) = cv2.boundingRect(l)
            (minX, maxX) = (min(minX, x), max(maxX, x + w))
            (minY, maxY) = (min(minY, y), max(maxY, y + h))

        # draw the bounding box
        cv2.rectangle(result, (minX, minY), (maxX, maxY),
            (0, 0, 255), 3)

    # increment the total number of frames read and draw the
    # timestamp on the image
    total += 1
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(result, ts, (10, result.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # show the output images
    cv2.imshow("Left Frame", left)
    cv2.imshow("Right Frame", right)
    cv2.imshow("Result", result)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()