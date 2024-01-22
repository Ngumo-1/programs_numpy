import numpy as np
from rand_int import (generate_array_randomly,
                      generate_number_randomly,
                      random_no_frm_given_range)
from rand_floats import generate_random_float
from rand_choice import random_choice

# size=[5]
# xarr=generate_array_randomly(1,6, size)
# print(xarr)
# shape=5
# float_s=generate_random_float(shape)
# print(float_s)
#
# rand_num=np.random.randint(1,7)
# print(rand_num)
# start=1
# stop=6
#
# rand_dice_face_label=generate_number_randomly(1, 6)
# print(rand_dice_face_label)
# size_tuple=(3,3,3)
# xarr=random_no_frm_given_range(1,3, size_tuple)
# print(xarr)

arr=np.array([1,2,3,4,5,6,7,8,9])
# xarr=np.random.choice(arr, )
shape=(2,2,2)



xarr=random_choice(arr,shape)
print(xarr)