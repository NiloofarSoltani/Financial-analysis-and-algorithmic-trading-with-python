import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_list = [1, 2, 3]
arr = np.array([1, 2, 3])
dic = {'a': 10, 'b': 20, 'c': 30}

print('Creating a Series Using Lists')
pd.Series(data=my_list, index=labels)
