import numpy as np
from numpy import random as rd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import timeit

total = 10
totals_array = np.array([])
pi_vals_per_total = np.array([])
time_per_total = np.array([])
angle = np.linspace(0, 2*np.pi, 150)
radius = 1
x = radius * np.cos(angle)
y = radius * np.sin(angle)


def CirclePlot(x_axis, y_axis):
    # Function to plot the scatter points in addition to the circle
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    ax.plot(x, y, color='r', linewidth=5)
    ax.scatter(x_axis, y_axis, s=1, c='black')
    plt.show()


def Plot(x_axis, y_axis, xlim_lo, xlim_hi, ylim_lo, ylim_hi, xlabel, ylabel):
    # Function to produce a linear plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    popt, pcov = curve_fit(Fit, x_axis, y_axis)
    plt.xlim(xlim_lo, xlim_hi)
    plt.ylim(ylim_lo, ylim_hi)
    plt.xlabel('{}'.format(xlabel))
    plt.ylabel('{}'.format(ylabel))
    plt.rcParams.update({'font.size': 20})
    ax.scatter(x_axis, y_axis, s=20)
    plt.plot(x_axis, Fit(x_axis, popt[0], popt[1]), linestyle='-', 
             color='black')
    plt.show()
    print('Slope = {:.3f} +- {:.3f}'.format(popt[0], np.sqrt(pcov[0, 0])))
    print('Intercept = {:.3f} +- {:.3f}'.format(popt[1], np.sqrt(pcov[1, 1])))


def Fit(x, m, c):
    return m*x+c


while total <= 3E6:
    pi_vals = np.array([])
    time_vals = np.array([])
    for i in range(10):
        execution_time = timeit.default_timer()
        circle_count = 0
        coord_array = np.array(rd.rand(total, 2))
        for i in range(total):
            position = np.sqrt((coord_array[i, 0])**2 + (coord_array[i, 1])**2)
            # Calculates radius of points from origin
            if position <= 1:
                circle_count += 1
        pi = (float(circle_count)/total) * 4
        pi_vals = np.append(pi_vals, pi)

        CirclePlot(coord_array[:, 0], coord_array[:, 1])
        time_taken = timeit.default_timer() - execution_time
        time_vals = np.append(time_vals, time_taken)
        print('The time taken to execute the code is {}'.format(time_taken))

    print("For {:.2e} random points, our best estimate of π is {:.5f}"
          .format(total, np.mean(pi_vals)))
    pi_vals_per_total = np.append(pi_vals_per_total, np.mean(pi_vals))
    time_per_total = np.append(time_per_total, np.mean(time_vals))
    totals_array = np.append(totals_array, total)
    total *= 2
residuals = (pi_vals_per_total - np.pi)/np.pi * 100
Plot(np.log10(totals_array), np.log10(abs(residuals)), 0, 7, -2.5, 0.8
     , 'log$_{10}$(Number of points)'
     , 'log$_{10}$(Percentage deviation from π)')
Plot(totals_array/1E6, time_per_total, 0, 2.5, 0, 16.5
     , 'Number of points (x10$^6$)', 'Time taken to calculate π (s)')
        