import numpy as np
import math
import time

def c(n):
    return np.array(range(int(-n/2),int(n/2+1)))

def r1(h):
    return max(1,abs(h))

def phi(x,n):   #book version: p. 78
    result = 0
    for h in c(n):
        result = result + ((1/r1(h))*np.exp(2*math.pi*complex(0,1)*h*x))
    return result

def precom(n): #precomputes the possible values for phi
    precomvalues = [0]*n
    for i in range(0,n):
        precomvalues[i] = phi(i/n,n)
    return precomvalues


    