from test import tools
import math
import numpy as np
import matplotlib.pyplot as plt

def mat(n):  #creates the matrix Omega_n
    prevalues = tools.precom(n)
    matrix = np.zeros(shape=(n-1,n))
    for i in range(1,n):
        for j in range(0,n):
            matrix[i-1,j]= prevalues[(i*j)%n].real
    return matrix

def plot_figure(matrix): #plots a colormap of a matrix 
    fig, ax = plt.subplots()
    ax.matshow(matrix, cmap=plt.cm.gnuplot)
    plt.show()

