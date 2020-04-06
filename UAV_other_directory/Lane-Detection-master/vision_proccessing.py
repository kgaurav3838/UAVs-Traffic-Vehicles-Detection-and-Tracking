import cv2
import numpy as np

def convert_to_gray(image:str):
    '''Convert image to the gray-scale version of itself

    PRECONDITION: image is the file name and location in directory for image

    POSTCONDITION: returns a gray-scale image'''

    raw_image = cv2.imread(image)
    gray = cv2.cvtColor(raw_image,cv2.COLOR_RGB2GRAY)
    return gray

def convert_to_gradient(image:str):
    '''Converts a gray-scale image to a gradient version of the same image

    PRECONDITION: image is the file name and location in directory for image

    POSTCONDITION: returns a gradient image'''

    gradient_image = cv2.Canny(image,50,150)
    return gradient_image

def hough_space(image:str,interval:float,precision:float, threshold:int, line_gap):
    '''Converts image to hough space (polar coordinates) to identify straight
    lines in gray image

    PRECONDITION: image is the file name and location in directory for image,
    interval is the number of pixels for one bin in the overlaying array,
    precision is the theta value for bin size and threshold is the number of
    intersecting points in a bin to be considered a line. line_gap is the
    distance two lines can be apart and still be considered one line

    POSTCONDITION: returns '''

    radian = 180/np.pi
    hough_image = cv2.HoughLinesP(image,interval,precision*radian,threshold,
                                  minLineLength=40,maxLineGap=line_gap)

    return hough_image

def display_lines(hough,image:str):
    '''Overlays where the computer thinks the lane lines are on image

    PRECONDITION: hough is the result from the hough_space function and
    image is the image where you are trying to find the lanes. This can be in
    color or gray scale

    POSTCONDITION: image with an overlay of where computer thinks lane markings
    are
    '''

    line_image = np.zeros_like(image)
    if hough != None:
        for line in hough:
            x1,x2,y1,y2 = line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

    combine = cv2.addWeighted(image,0.8,line_image,1,1)
    return combine





