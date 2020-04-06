# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

from __future__ import print_function, division

import numpy as np
import pandas as pd
from ex8 import get_spiral

# Note: you may need to update your version of future
# sudo pip install -U future

# get the data
X, Y = get_spiral()

# combine the data into one array
# data to be concatenated must have same # of dimensions
# e.g. N x D and N x 1
# not  N x D and N
data = np.concatenate((X, np.expand_dims(Y, 1)), axis=1)

df = pd.DataFrame(data)
df.columns = ['x1', 'x2', 'y']
df.to_csv('mydata.csv', index=False)