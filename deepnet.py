import pandas as pd
import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Input, Dropout
from sklearn.model_selection import train_test_split

bed = np.load("C:/Users/Vasvi/Desktop/bed.npy")
bat = np.load("C:/Users/Vasvi/Desktop/bat.npy")
beard= np.load("C:/Users/Vasvi/Desktop/beard.npy")
apple = np.load("C:/Users/Vasvi/Desktop/apple.npy")
clock = np.load("C:/Users/Vasvi/Desktop/clock.npy")
banana = np.load("C:/Users/Vasvi/Desktop/banana.npy")
cake = np.load("C:/Users/Vasvi/Desktop/cake.npy")

data_x=[]
for i in range(10000):
    data_x.append(cake[i])
for i in range(10000):
    data_x.append(beard[i])
for i in range(10000):
    data_x.append(bed[i])
for i in range(10000):
    data_x.append(bat[i])
for i in range(10000):
    data_x.append(apple[i])
for i in range(10000):
    data_x.append(clock[i])
for i in range(10000):
    data_x.append(banana[i])


data_x1 = np.array(data_x)
data_x1=data_x1/255.0
print(data_x1.shape)

data_y=[]
for i in range(10000):
    data_y.append(0)
for i in range(10000):
    data_y.append(1)
for i in range(10000):
    data_y.append(2)
for i in range(10000):
    data_y.append(3)
for i in range(10000):
    data_y.append(4)
for i in range(10000):
    data_y.append(5)
for i in range(10000):
    data_y.append(6)

data_y=np.array(data_y)

data_y = np_utils.to_categorical(data_y)


predmodel = Sequential()

predmodel.add(Dense(512, input_shape=(784,), activation='relu'))
predmodel.add(Dense(512, activation='relu'))
predmodel.add(Dense(7, activation='softmax'))

predmodel.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

predmodel.fit(data_x1, data_y, epochs=30, batch_size=100)