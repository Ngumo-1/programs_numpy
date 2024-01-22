import numpy as np
from numpy import random

# arr=np.array([1,2,3,4,5])
# print(arr)
#
# xarr=np.random.randint(1,6, size=([5]))
# print(xarr)

def generate_array_randomly(start_number, end_number, size):
    arr=np.random.randint(start_number, end_number, size=size)
    return arr
def generate_number_randomly(start, stop):

    return np.random.randint(start, stop+1)