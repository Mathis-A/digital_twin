a=[(1,1),(5,0),(2,0),(1,-1)]


import numpy as np

a=np.array(a)

assert a.shape[1]==2
assert len(a.shape)==2

print(list(np.array(a).flatten()))