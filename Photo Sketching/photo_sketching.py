import cv2
import sys

#read image
image = cv2.imread("./test.jpg")

#check if image exists
if image is None:
    print('can not findimage')
    sys.exit()

#convert to gray scale
img_gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#invert the gray image
img_invert = 255 - img_gray

#apply gaussian blur
img_invert = cv2.GaussianBlur(img_invert, (21, 21), 0)

#blend using color dodge
output = cv2.divide(img_gray, 255-img_invert, scale=256.0)

#create windows to display image
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Pencil Sketch", cv2.WINDOW_AUTOSIZE)

cv2.imshow('Image', image)
cv2.imshow('Pencil Sketch', output)

cv2.waitKey(0)
cv2.destroyAllWindows()