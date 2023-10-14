import cv2

img=cv2.imread("butterfly.jpg")
grayscale=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("butterfly",grayscale)
print(grayscale)
cv2.waitKey(0)