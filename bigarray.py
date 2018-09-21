import numpy as np
'''line Sapace generates an 1d array with interval first'''
array=np.linspace(0,10,10000).reshape(1000,10)
print('Length',len(array))
print('# of rows',np.size(array,0))
print('# of col',np.size(array,1))
print('Array Shape',array.shape)
print(array)
print()

#print('Split:\n',np.hsplit(array,))