#-----------import libraries---------------
import cv2

#-------------read original img-------------
img = cv2.imread('./test.jpg')

#--------------display original img---------
cv2.imshow('Original', img)
cv2.waitKey(0)

#---------------convert to grayscale--------------
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#----------blur img for edge detection----------
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

#------------sobel edge detction--------
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

#----------detect sobel edge detection images------------
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function',sobelxy)
cv2.waitKey(0)

#----------Canny Edge Detection-------
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

#------------Display Canny Edge Detection Image---------
cv2.imshow('Canny Edge Detection',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()