import numpy as np

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("array of 1s: ", np.ones(20))

print("empty array: ", np.empty(2))

print("array of a certain range", np.arange(5))

print("array spaced evenly", np.linspace(0, 10, 4))

a = np.random.rand(5)
print("array with random values: ", a)

print("sorted previous array: ", np.sort(a))

#concatenate 2
c = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

d = np.concatenate((c, b))
print("concatenated array: ", d)

print()
print()
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print("Array: ", "\n",  array_example)

print("Dimension of Array: ", array_example.ndim)
print("Size of array: ", array_example.size)
print("Shape of array: ", array_example.shape)

print()
ex = np.array([1, 2, 3, 4, 5, 6])
print("Example array: ", ex)
v = ex[np.newaxis, :] #can be added in col too
print("Adding axis", v, v.shape) #also with np.expand_dims(array, which axis)

data = np.array([1, 2, 3])
print("First dim", data[1])
print("first dim multiple", data[0:2])
print("divisibile by 2 elements or 1", data[(data%2==0) | (data ==1)])
print("split evenly array", np.hsplit(data, 3))
print("deep copy: ", data.copy())
 
#add, subtract, multiplyu, and divide with respective signs

data = np.array([1.0, 2.0, 2, 4, 6, 6, 18])
data *= 1.6
print("broadcasted array", data)

#for statistics use min, max, sum, std, and mean for respective parts

print("find unique element in array: " , np.unique(data))
print("transpose array", data.T)
print("reverse above array", np.flip(data))

print()
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("new array", "\n", arr_2d)
reversedarr = np.flip(arr_2d, axis = 0)
print("reverse only rows", "\n", reversedarr)
print("reverse only columns:" ,'\n',  np.flip(arr_2d, axis=1))
print("reverse a certain column", "\n", np.flip(arr_2d[:,1]))
print("reverse certain row", "\n", np.flip(arr_2d[1]))


print("flatten() and ravel()", arr_2d.flatten(), "ravel changes parent")