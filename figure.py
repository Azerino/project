from test import tools
import math
import numpy as np
import matplotlib.pyplot as plt

def mat(n):  #erstellt die Matrix Omega_n
    prevalues = tools.precom(n)
    matrix = np.zeros(shape=(n-1,n))
    for i in range(1,n):
        for j in range(0,n):
            matrix[i-1,j]= prevalues[(i*j)%n].real
    return matrix

def plot_figure(matrix): #plottet eine colormap der zu der Matrix 
    fig, ax = plt.subplots()
    ax.matshow(matrix, cmap=plt.cm.gnuplot)
    plt.show()

