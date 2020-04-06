# https://deeplearningcourses.com/c/deep-learning-prerequisites-the-numpy-stack-in-python
# https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python

from __future__ import print_function, division

from builtins import range

import matplotlib.pyplot as plt
import numpy as np


# Note: you may need to update your version of future
# sudo pip install -U future

def sampleY(n=1000):
  # draw n samples from uniform dist.
  X = np.random.random(n)
  Y = X.sum()
  return Y


# now draw N Y's
N = 1000
Y_samples = np.zeros(N)
for i in range(N):
  Y_samples[i] = sampleY()


# now plot the Y_samples
plt.hist(Y_samples, bins=20)
plt.show()