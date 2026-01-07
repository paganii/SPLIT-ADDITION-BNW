import cv2

img4 = cv2.imread("spiderman.png", 1) #color, grayscale, unchanged - 1 
cv2.imshow("original", img4)
print(img4)
#splitting the image in bgr saturation
b, g, r = cv2.split(img4)
cv2.imshow("Blue Saturation", b)
cv2.waitKey(0)
cv2.imshow("Green Saturation", g)
cv2.waitKey(0)
cv2.imshow("Red Saturation", r)
cv2.waitKey(0)
