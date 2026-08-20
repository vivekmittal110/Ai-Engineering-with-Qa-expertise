# normalize an array

import numpy as np
arr = np.array([10,20,30,40,50],dtype=float)

mini = np.min(arr)
maxx = np.max(arr)
# for i in range(len(arr)):
#     arr[i] = (arr[i]- mini)/(maxx-mini)
# print(arr)

# best way
normalize = (arr- mini)/(maxx-mini)
print(normalize)