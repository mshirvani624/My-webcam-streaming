import cv2
import numpy as np
import matplotlib as plt

img=cv2.imread("scary-lion.png")
print(img.shape)
# img[:,:,0]=255
img=cv2.resize(img,(640,480))
# print(cv2.COLOR_BGR2GRAY)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray.shape)
# img=arr4.astype(np.uint8)


# img[195:205,500:600]=0
cv2.imshow("Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('hello')
