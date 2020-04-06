from vision_proccessing import *

def main():
    gray = convert_to_gray('test_image.jpg')
    gradient = convert_to_gradient(gray)
    hough = hough_space(gradient,2,1,100,5)
    display = display_lines(hough,gray)
    cv2.imshow('result', display)
    cv2.waitKey(0)

main()
