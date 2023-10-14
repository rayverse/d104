import cv2
import numpy as np

black=np.zeros([6,6])
#print(black)
#cv2.imshow("black image", black)
black[2:4,2:4]=255
print(black)
cv2.imshow("black image", black)
cv2.waitKey(0)