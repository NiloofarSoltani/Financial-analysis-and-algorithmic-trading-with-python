import numpy as np

print('A list of even numbers with numpy:', np.arange(0, 11, 2))
print('A list of odd numbers with numpy:', np.arange(1, 11, 2))
print('A list k zeros with numpy:', np.zeros(3))
print('A list k ones with numpy:', np.ones((3, 4)))
print('A list of k _evenly spaced_ numbers between a and b np.linspace(a,b,k):', np.linspace(0, 10, 4))
print('51 = k a=0 b=10, bcz of index start from 0 ', np.linspace(0, 10, 51))
print('50 = k a=0 b=10', np.linspace(0, 10, 50))
print('identity matrix is a square matrix where diagonal is one ', np.eye(4))
print('a uniformd istribution  over [0,1) (all the number between 0 and 1 has the same probability to picked)',
      np.random.rand(2, 2))
print('random integer', np.random.randint(1, 100, 10))
arr = np.arange(25)
randarr = np.random.randint(0, 60, 25)
print(arr, 'a quick way to create a matrix', arr.reshape(5, 5))
print(randarr, 'a quick way to create a matrix', randarr.reshape(5, 5))
print('The max number in the array is ', randarr.max())
print('The index of max number in the array is ', randarr.argmax())
print('The min number in the array is ', randarr.min())
print('The index min of a number in the array is ', randarr.argmin())
arrr = np.arange(24)
print(arrr, '\n\nChanging array to matrix is possible with reshape method: arrr.reshape(6,4)=', arrr.reshape(6, 4))
print('Or different shape: arrr.reshape(4,6)=', arrr.reshape(4, 6))

# Numpy Operations
arropt = np.arange(2, 12)
print('\n\nNumpy Operations\n', arropt)
print(arropt + arropt)
print(arropt * arropt)
print(arropt / arropt)
print(arropt - arropt)
print(arropt ** 2)
print(arropt + 100)
print(np.sqrt(arropt))
print(np.exp(arropt))

# Numpy Indexing and Selection
arrin = np.arange(0, 11)
print('\n\nNumpy Indexing and Selection\n', arrin[8])
print(arrin[1:5])
print(arrin[:5])
print(arrin[3:])
arrin[3:5] = 100
print('Brodcasting: ', arrin)
arrind = arrin[5:]
print('cuting a part of an array:', arrind)
print(arrin, arrind)
arrind[:] = 100
print('This is a pointer to the original array not a copy of the elements:useful for memory usage for big dataset!\n',
      'arrin:', arrin, 'arrind(pointer to original arrin):', arrind)
arrin2 = np.arange(0, 11)
arrind_copy = arrin2.copy()
arrind_copy[:] = 100
print('arrin:', arrin2, 'arrind_copy will not change the original array', arrind_copy)

# mat[row,column] == mat[row][column]
mat = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
print('\n\nNumpy Operations\n')
print('selecting the first row of the matrix(nested array we created above)**mat[0]** is :', mat[0])
print('selecting 22 of the matrix(nested array we created above)**mat[1][1]** is :', mat[1][1])
print('mat[1,1] == is the same as == mat[1,1]** is :', mat[1, 1])
print('if we want a part of a mat like only [22 23][32 33]**mat[1:,1:]', mat[1:, 1:])

# Conditional selection
ary = np.arange(1, 11)
print('\n\nConditional selection\n', ary > 4)
print('to show the array elements we create a var and we put it in the array: bol_ary=ary>4 --> ary[bol_ary] ')
bol_ary = ary > 4
print(ary[bol_ary])
print('but this is a better way : ary[aray>4]', ary[ary > 4])

# Exercise
print('\n\nExercise\n')
print('\nCreate an array of all the even integers from 10 to 50')
# print(np.arange(10, 51, 2))
print('\nCreate a 3x3 matrix with values ranging from 0 to 8')
# print(np.arange(9).reshape(3, 3))
print('\nCreate a 3x3 identity matrix')
# print(np.eye(3))
print('\nUse NumPy to generate a random number between 0 and 1')
# print(np.random.rand())
print('\nUse NumPy to generate an array of 25 random numbers sampled from a standard normal distribution')
# print(np.random.randn(25))
print('\nCreate the following matrix:\n', np.arange(1, 101).reshape(10, 10) / 100)
# print(np.linspace(0, 1, 101), 'but this is not a MATRIX it is an ARRAY')
print('\nCreate an array of 20 linearly spaced points between 0 and 1:')
# print(np.linspace(0,1,20))

print('HERE IS THE GIVEN MATRIX CALLED MAT.USE IT FOR THE FOLLOWING TASKS')
# print(np.arange(1,26).reshape(5,5))
# mat=np.arange(1,26).reshape(5,5)
print('write the code that give this array [12 13 14 15][17 18 19 20][22 23 24 25]')
# print(mat[2:,1:])
print('write the code that give number 20')
# print(mat[3,-1])
print('write the code that give this array [2][7][12]')
# print(mat[:3,1])
# print(mat[:3,1:2])
print('write the code that give this array [21 22 23 24 25]')
# print(mat[-1,:])
print('write the code that give this array  [16 17 18 19 20][21 22 23 24 25]')
# print(mat[3:,:])
print('write the code that Get the sum of all the values in mat')
# print(mat.sum())
print('write the code that Get the standard deviation of the values in mat')
# print(mat.std())
print('Get the sum of all the columns in mat')
# print(mat.sum())
# print('sum of the first row: ',mat.sum(axis=1))
# print('sum of the first column: ',mat.sum(axis=0))


