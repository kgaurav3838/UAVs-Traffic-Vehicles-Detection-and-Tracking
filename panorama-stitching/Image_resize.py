# Image resizing using cv2.resize
import cv2
#Read the images from your directory
image1=cv2.imread('images/left1.jpg',cv2.IMREAD_COLOR)  # Left Image
scale_percent = 80  # percent of original size
width = int(image1.shape[1] * scale_percent / 100)  #image1.shape return (width x height x channel) or (row x column x channel)
height = int(image1.shape[0]* scale_percent / 100)
dim = (width, height)
image2=cv2.resize(image, dim, interpolation = cv2.INTER_AREA)   #ReSize image
cv2.imshow("Original_image",image)
cv2.imshow("Resized_image",image2)
cv2.waitKey()
cv2.destroyAllWindows()

