import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt
import timeit

total = 10
totals_array = np.array([])
pi_vals_per_total = np.array([])
angle = np.linspace(0, 2*np.pi, 150)
radius = 1
x = radius * np.cos(angle)
y = radius * np.sin(angle)


def ScatterPlot(x_axis, y_axis):
    # Function to plot the scatter points in addition to the circle
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    ax.plot(x, y, color='r', linewidth=5)
    ax.scatter(x_axis, y_axis, s=1, c='black')
    plt.show()


def LinearPlot(x_axis, y_axis, xlabel, ylabel):
    # Function to produce a linear plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    plt.xlabel('{}'.format(xlabel))
    plt.ylabel('{}'.format(ylabel))
    plt.rcParams.update({'font.size': 20})
    ax.scatter(x_axis, y_axis, s=20)
    plt.show()


while total <= 1E6:
    pi_vals = np.array([])
    for i in range(10):
        execution_time = timeit.timeit(number=total)
        circle_count = 0
        coord_array = np.array(rd.rand(total, 2))
        for i in range(total):
            position = np.sqrt((coord_array[i, 0])**2 + (coord_array[i, 1])**2)
            # Calculates radius of points from origin
            if position <= 1:
                circle_count += 1
        pi = (float(circle_count)/total) * 4
        pi_vals = np.append(pi_vals, pi)

        ScatterPlot(coord_array[:, 0], coord_array[:, 1])
        print(execution_time)

    print("For {:.0e} random points, our best estimate of π is {:.5f}"
          .format(total, np.mean(pi_vals)))
    pi_vals_per_total = np.append(pi_vals_per_total, np.mean(pi_vals))
    totals_array = np.append(totals_array, total)
    total *= 10
residuals = (pi_vals_per_total - np.pi)/np.pi * 100
print(np.abs(residuals))
LinearPlot(np.log10(totals_array), abs(residuals)
           , 'log$_{10}$(Number of points)', 'Percentage deviation from π')
        