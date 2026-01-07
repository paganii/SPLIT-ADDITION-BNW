import cv2

img1 = cv2.imread("spiderman.png", 1) #color, grayscale, unchanged - 1 
img2 = cv2.imread("hulk.png", 1) #color, grayscale, unchanged - 1 
sum = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow("sum", sum)
cv2.imwrite("combo.png", sum)
cv2.waitKey(0)