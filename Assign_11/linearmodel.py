import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1,input_shape =[1])])
model.compile(optimizer ='sgd',loss = 'mean_squared_error')

#y = 4x-6

xs = np.array([-2,-1,0,1,2,3,4,5,6],dtype = float)
ys = np.array([-14,-10,-6,-2,2,6,10,14,18],dtype = float)

model.fit(xs,ys,epochs = 1000)

print("expect output of approx. 394 ")
print(model.predict([100]))
