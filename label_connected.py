import numpy as np
import pandas as pd
import os
import cv2
from matplotlib import pyplot as plt
print cv2.__version__


def get_connected_components(bin_image, connectivity = 4):
    '''
    Method: One component at a time connected component labeling 
        Input: Binary Image (h x w array of 0 and non-zero values, will created connected components of non-zero)
        Returns: connected_array -(h x w array where each connected component is labeled with a unique integer (1:counter-1)
                counter-1 - integer, number of unique connected components
    '''
    h,w = bin_image.shape
    yc, xc  = np.where(bin_image!=0)
    queue = []
    connected_array = np.zeros((h,w)) #labeling array
    counter = 1
    for elem in range(len(xc)):
        # iterate over all nonzero elements
        i = yc[elem] 
        j = xc[elem]
        if connected_array[i,j] == 0:
            # not labeled yet proceed
            connected_array[i,j] = counter
            queue.append((i,j))
            while len(queue) != 0:
                # work through queue
                current = queue.pop(0)
                i,j = current
                if i == 0:
                    coords = np.array([[i, i, i+1],[j-1, j+1, j]])
                elif i == h - 1:
                    coords = np.array([[i, i, i-1],[j-1, j+1, j]])
                elif j == 0:
                    coords = np.array([[i, i+1, i-1],[j+1, j, j]])
                elif j == w - 1:
                    coords = np.array([[i, i+1, i-1],[j-1, j, j]])
                else:
                    coords = np.array([[i, i, i+1, i-1],[j-1, j+1, j, j]])
                for k in range(len(coords[0])):
                    # iterate over neighbor pixels, if  not labeled and not zero then assign current label 
                    if connected_array[coords[0,k], coords[1,k]] == 0 and bin_image[coords[0,k], coords[1,k]] != 0:
                       connected_array[coords[0,k], coords[1,k]] = counter
                       queue.append((coords[0,k], coords[1,k]))
            counter += 1
    
    return connected_array, counter-1

    
    
    
def test():
    test_arr = np.zeros((8,8))
    test_arr[1:3,1:3] = 1
    test_arr[3:5,3:5] = 1
    test_arr[6,1] = 1
    test_arr[6,5:7] = 1
    test_arr[7,3:5] = 1
    print test_arr
    connected_arr, count = get_connected_components(test_arr)
    print connected_arr
if __name__ == "__main__":
    test()