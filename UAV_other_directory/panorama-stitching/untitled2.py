# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:14:48 2020

@author: kumar
"""

# USAGE
# python untitled2.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
import argparse

import cv2
import imutils

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")

ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

