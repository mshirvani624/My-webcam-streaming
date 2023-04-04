import numpy as np

arr1=np.ones((3,4))
arr2=np.array([3,4])

arr1[2,1:3]=arr2
print(arr1)