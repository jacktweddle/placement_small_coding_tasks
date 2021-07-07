import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt

total = 10
angle = np.linspace(0,2*np.pi,150)
radius = 1
x = radius * np.cos(angle)
y = radius * np.sin(angle)

while total<=1E5:
    circle_count = 0
    coord_array = np.array(rd.rand(total,2))
    for i in range(total):
        position = np.sqrt((coord_array[i,0])**2 + (coord_array[i,1])**2) 
        #Calculates radius of points from origin
        if position <= 1:
            circle_count += 1
    pi = (float(circle_count)/total) * 4
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    plt.xlim(0,1)
    plt.ylim(0,1)
    ax.plot(x,y,color='r')
    ax.scatter(coord_array[:,0],coord_array[:,1],s=1,c='black')
    plt.show()

    print("For {} random points, our estimate of π is {:.5f}".format(total, pi))
    
    total *= 10
    
    