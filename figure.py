from test import tools
import math
import numpy as np

def mat(n):  #erstellt die Matrix Omega_n
    prevalues = tools.precom(n)
    matrix = np.zeros(shape=(n-1,n))
    for i in range(1,n):
        for j in range(0,n):
            matrix[i-1,j]= prevalues[(i*j)%n]
    return matrix

