import numpy as np

x = np.array([1, 2, 3])
print(x.shape) 
result = np.expand_dims(x, axis=0)
print(result)
print(result.shape)