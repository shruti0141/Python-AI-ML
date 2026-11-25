
import numpy as np

nums= np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

#print(nums[1:4])

#print(nums[:3])#exact values

#print(nums[3:])#exact values
#print(nums[:])
#print(nums[::2])
w=np.array([.3, .4, .7, .8])

s=np.dot(nums,w)
print(s)




