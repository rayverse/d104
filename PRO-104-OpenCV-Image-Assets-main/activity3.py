import cv2

img2=cv2.imread("poster.jpg")

rocket=img2[120:360,400:500]
img2[0:240,500:600]=rocket
cv2.putText(img2,"Helloo", (20,200), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,255))
cv2.imshow("output", img2)
cv2.waitKey(0)