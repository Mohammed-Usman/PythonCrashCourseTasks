from keras.model import Sequential
from keras.layers import Dense
from keras.optimizers import Adam,SGD

%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df  = pd.read_csv('../data/weight-height.csv')
X = df[['Height']].values
y_true = df[['Weight']].values

model = Sequential()

#model.add(Dense(1,input_shape(1,))

model.add(Dense(4,input_shape(1,))
model.add(Dense(4,input_shape(4,))
model.add(Dense(1,input_shape(4,))
          
model.compile(Adam(lr=0.8),'mean_squared_error')
          
model.fit(X,y_true,epochs=40)


''' performance of model
    Classification
    Linear Regression'''
          
