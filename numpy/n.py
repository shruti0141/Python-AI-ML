import numpy as np

arr = np.array([
    [70, 80, 90],
    [ 60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])

"""print(arr.size)# how many elements are there
print(arr.shape)

print(arr[:2,-1])

#to calculate mean value in 2d we use axis parameter
#axis1=horizontal across each row
#axis 0= vertical across each column
print(np.mean(arr, axis=0))
a=np.mean(arr, axis=1) 
print(np.round(a,2))# this is use to roundup the values ex:12.5=13,12.3=12
#dot=it performs std  matrix multiplication 2D=m1,m2  np.dot(m1,m2)
#here m1=arr & m2=(.3,.3, .4)"""
w= np.array([.3, .3, .4])
z= np.dot(arr,w)

print(z)

print(np.arange(12).reshape(3,4))