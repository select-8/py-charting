#%%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# a = np.array([(1,2,3),(3,4,5)])
# b = np.array([(2,3,4),(5,6,7)])
# a = np.array([(1,2,3,5),(3,4,5,6),(7,8,9,10)])

# a = a.reshape(4,2)

# print (a[0:,-1])

# a = np.linspace(1,10,5)

# a = np.array([1,2,3])

# print (a.max())
# print (a.min())
# print (a.sum())
# print (a.sum(axis=0))
# print (a.sum(axis=1))
# print (np.sqrt(a))
# print (np.sqrt(a[0:,-1].sum()))
# print (np.std(a))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# print(a.ravel())

x = np.arange(0,3*np.pi, 0.1)

y = np.tan(x)

plt.plot(x,y)

plt.show

#%%


#%%
