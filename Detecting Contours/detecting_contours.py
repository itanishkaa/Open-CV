import cv2

image = cv2.imread('./test.jpg')

blue, green, red = cv2.split(image)

img_gray = cv2.cvtColor(
    image, 
    cv2.COLOR_BGR2GRAY
)

ret, thresh = cv2.threshold(
    img_gray, 
    150, 
    255, 
    cv2.THRESH_BINARY
)

image_copy = image.copy()
image_contour_blue = image.copy()
image_contour_green = image.copy()
image_contour_red = image.copy()

contours, hierarchy = cv2.findContours(
    image=thresh, 
    mode=cv2.RETR_TREE, 
    method=cv2.CHAIN_APPROX_NONE
)

contours1, hierarchy1 = cv2.findContours(
    image=blue,
    mode=cv2.RETR_TREE,
    method=cv2.CHAIN_APPROX_NONE
)

contours2, hierarchy2 = cv2.findContours(
    image=green, 
    mode=cv2.RETR_TREE, 
    method=cv2.CHAIN_APPROX_NONE
)

contours3, hierarchy3 = cv2.findContours(
    image=red, 
    mode=cv2.RETR_TREE, 
    method=cv2.CHAIN_APPROX_NONE
)

cv2.drawContours(
    image=image_copy, 
    contours=contours, 
    contourIdx=-1, 
    color=(0,255,0),
    thickness=2,
    lineType=cv2.LINE_AA
)

cv2.drawContours(
    image=image_contour_blue, 
    contours=contours1, 
    contourIdx=-1, 
    color=(0, 255, 0), 
    thickness=2, 
    lineType=cv2.LINE_AA
)

cv2.drawContours(
    image=image_contour_green, 
    contours=contours2, 
    contourIdx=-1, 
    color=(0, 255, 0), 
    thickness=2, 
    lineType=cv2.LINE_AA
)

cv2.drawContours(
    image=image_contour_red, 
    contours=contours3, 
    contourIdx=-1, 
    color=(0, 255, 0), 
    thickness=2, 
    lineType=cv2.LINE_AA
)

cv2.imshow('Binary image', thresh)
cv2.imshow('None approximation', image_copy)
cv2.imshow('Contour detection using blue channels only', image_contour_blue)
cv2.imshow('Contour detection using green channels only', image_contour_green)
cv2.imshow('Contour detection using red channels only', image_contour_red)

cv2.waitKey(0)
cv2.destroyAllWindows()