# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:21:30 2020
@author: KGaurav
"""
# python realtime_stitching.py  # Video Stitching

# import the necessary packages
from __future__ import print_function

import datetime
import time

import cv2
# from imutils.video import VideoStream
import numpy as np
from imagesearch.basicmotiondetector import BasicMotionDetector
from imagesearch.panorama import Stitcher

# initialize the video streams and allow them to warmup
print("[INFO] starting videos...")

#video1= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-2/2.mp4"   # Home
#video2= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-2/3.mp4"   # Home
#video1= "R:/My Files/OneDrive - IIT Kanpur\IITK OneDrive\Videos/video-data-2/2.mp4"   # Work
#video2= "R:/My Files/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-2/3.mp4"  # Work
#video1= "E:/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"  # Home
#video2= "E:/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 2/DJI_0152.MOV"
video1= "R:/My Files/OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 1/DJI_0006.MOV"  # Work
video2= "R:/My Files//OneDrive - IIT Kanpur/Video Data/Airstrip test/Drone 2/DJI_0152.MOV"
#video1= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-3/first.mp4"
#video2= "E:/OneDrive - IIT Kanpur/IITK OneDrive/Videos/video-data-3/third.mp4"

#leftStream = VideoStream(video1).start()
#rightStream = VideoStream(video2).start()
leftStream=cv2.VideoCapture(video1)
rightStream = cv2.VideoCapture(video2)

time.sleep(2.0)
# initialize the image stitcher, motion detector, and total number of frames read
stitcher = Stitcher()
motion = BasicMotionDetector(minArea=500)
total = 0
print("[INFO] Video Stitching is in progress...")
# loop over frames from the video streams
while True:
    # grab the frames from their respective video streams
    _, left = leftStream.read()
    _, right = rightStream.read()

    #left = cv2.imread(leftStream)
    #right = cv2.imread(rightStream)

    # resize the frames
    #left = imutils.resize(left, width=400)
    #right = imutils.resize(right, width=400)
    #print("Original Dimensions : ", left.shape, right.shape)
    scale_percent = 30  # percent of original size
    width_left = int(left.shape[1] * scale_percent / 100)
    height_left = int(left.shape[0])
    width_right = int(right.shape[1] * scale_percent / 100)
    height_right = int(right.shape[0])
    dim_left = (width_left, height_left)
    dim_right = (width_right, height_right)
    left = cv2.resize(left, dim_left, interpolation = cv2.INTER_AREA)
    right = cv2.resize(right, dim_right, interpolation = cv2.INTER_AREA)

    # stitch the frames together to form the panorama
    # IMPORTANT: you might have to change this line of code
    # depending on how your cameras are oriented; frames
    # should be supplied in left-to-right order
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
    cv2.imshow("Result", result)
    cv2.imshow("Left Frame", left)
    cv2.imshow("Right Frame", right)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
leftStream.stop()
rightStream.stop()