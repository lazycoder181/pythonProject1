import numpy as np
from numpy.random import randn

N=1000
counter = 0

for i in randn(100):
    if i > -1 and i < 1:
        counter = counter + 1
print(counter/N)