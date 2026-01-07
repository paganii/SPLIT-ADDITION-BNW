import cv2
import os

img = cv2.imread("pikachu.png", cv2.IMREAD_COLOR) #color, grayscale, unchanged - 1 
cv2.imshow("pikachu", img)

path = "C:/Users/Hp/OneDrive/Desktop"
img2 = cv2.imread("pikachu.png", 0)
cv2.imshow("Pikachu in black and white", img2)
cv2.waitKey(0)
cv2.imwrite("Pikachuinblackandwhite.png", img2)
img2 = cv2.imread("pikachu.png", 0)
cv2.waitKey(0)

img4 = cv2.imread("spidermann.png", 1) #color, grayscale, unchanged - 1 
cv2.imshow("original", img4)
#splitting the image in bgr saturation
b, g, r = cv2.split(img4)
cv2.imshow("Blue Saturation", b)
cv2.waitKey(0)
cv2.imshow("Green Saturation", g)
cv2.waitKey(0)
cv2.imshow("Red Saturation", r)
cv2.waitKey(0)

cv2.destroyAllWindows()
