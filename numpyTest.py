import numpy as np
singledimensionarray = np.array([0, 1])  # 1
twodimensionarray = np.array(
    [
        [[0, 0, 0], [0, 0, 0]],
        [[1, 1, 1], [1, 1, 1]]
    ])  # 2x2
threedimensionarray = np.array(
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    ])  # 3x3x3
fourdimensionarray = np.array(
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]],
        [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]
    ])  # 4x4x4x4

def printarrayinfo(array):
    print(array)
    print('Dim ', array.ndim)
    print('Shape ', array.shape)
    print('Length ', len(array))

printarrayinfo(singledimensionarray)
#printarrayinfo(twodimensionarray)
#printarrayinfo(threedimensionarray)
#printarrayinfo(fourdimensionarray)