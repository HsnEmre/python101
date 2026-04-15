import numpy as np

data=np.loadtxt('data.txt',delimiter=' ')
rows_sum=np.sum(data,axis=1)


np.savetxt('output,txt',rows_sum,fmt="%d")



print(data)
print(rows_sum)
