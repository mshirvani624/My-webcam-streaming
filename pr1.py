import cv2
import numpy as np
import matplotlib as plt

arr1=np.ones((500,1000))*202
arr2=np.ones((500,1000))*56
arr3=np.ones((500,1000))*156

arr4=np.zeros((500,1000,3))

arr4[:,:,0]=arr1
arr4[:,:,1]=arr2
arr4[:,:,2]=arr3

img=arr4.astype(np.uint8)


img[195:205,500:600]=0
cv2.imshow("Image",img)
cv2.waitKey(0)
# cv2.destroyAllWindow("Image")

print('hello')
