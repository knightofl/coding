import numpy as np

aa = {'a':1, 'b':2}
bb = np.array(aa)

print(aa, type(aa))
print(bb, type(bb), bb.shape, bb.ndim, bb.dtype)

cc = np.ones((4,3))
print(cc, cc.dtype)

dd = cc.astype(int)
print(dd, dd.dtype)

ee = cc.astype('int')
print(ee, ee.dtype)

#ff = cc.astype(int8)
#print(ff, ff.dtype)

gg = cc.reshape(2,6)
print(gg)

hh = cc.reshape(-1, 4)
print(hh)

ii = np.arange(10)
print(ii)

print(ii.reshape(-1,2))
