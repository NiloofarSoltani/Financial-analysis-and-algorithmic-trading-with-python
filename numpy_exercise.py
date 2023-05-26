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
randarr = np.random.randint(0, 10, 10)
print(arr,'a quickly create a matrix',arr.reshape(5,5))