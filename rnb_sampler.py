import numpy as np
import random
from numpy import array
import traceback

def sampler(np_arr, clip_len, num_clips):
    # input validation
    if num_clips == 0:
        return None
    if clip_len * num_clips + (num_clips-1) > np_arr.shape[0]:
        print("Invalid input(array should be bigger!)")
        return 

    # find first possible combination
    max_space = int(np.floor((np_arr.shape[0] - clip_len * num_clips)/(num_clips-1)))
    first_combi = None
    idx = 1
    while idx + clip_len - 1<= np_arr.shape[0]:
        tmp = np.arange(idx, idx+clip_len)
        if first_combi is None:
            first_combi = np.empty_like(tmp)
            np.copyto(first_combi, tmp)
        else:
            first_combi = np.vstack((first_combi, tmp))
        idx += clip_len + max_space
    
    #stride over
    num_strides = np_arr.shape[0] - first_combi[first_combi.shape[0]-1, first_combi.shape[1]-1]
    result = []
    for i in range(num_strides+1):
        result.append(first_combi+np.full((first_combi.shape[0], first_combi.shape[1]), i, dtype=int))
    
    return np.array(result)    

while True:
    try:
        # get input
        a, b = map(int, input("2 numbers for video sequence: ").split())
        np_arr = np.arange(a, b)
        print(np_arr)
        clip_len = int(input("clip_length: "))
        num_clips = int(input("num_clips: "))

        output = sampler(np_arr, clip_len, num_clips)
        print("\n-----------------------Output-----------------------\n", output)
    except(ValueError):
        print(traceback.format_exc())
        break
print("Bye!")
