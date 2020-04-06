# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

import argparse

import cv2
import imutils
# import the necessary packages
from imagesearch.panorama import Stitcher

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--first", required=True, help="path to the first image")
ap.add_argument("--second", required=True, help="path to the second image")
ap.add_argument("--output", required=True, help="path to the output image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
while True:
    imageA = imutils.resize(imageA, width=800)
    imageB = imutils.resize(imageB, width=800)

# stitch the images together to create a panorama
    stitcher = Stitcher()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
    cv2.imshow("Image A", imageA)
    cv2.imshow("Image B", imageB)
    cv2.imshow("Keypoint Matches", vis)
    cv2.imshow("Result", result)
#Save output imgage
    cv2.imwrite(args["output"], result)
#cv2.waitKey(0)  # Press any key to break or exit
    key = cv2.waitKey(1) & 0xFF
# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break



