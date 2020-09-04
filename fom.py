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

def fom(g,n):  #book version: p. 78
    result = 0
    for i in np.array(range(0,n)):
        helper = 1 
        for x in g:
            helper = helper * phi(i*x/n,n)
        result = result + helper
    merit =  result/n-1
    if merit.imag < 10e-15:
        return merit.real
    return "Error, figure of merit has a complex part"

def precom(n): #precomputes the possible values for phi
    precomvalues = [0]*n
    for i in range(0,n):
        precomvalues[i] = phi(i/n,n)
    return precomvalues

def fom_precom(g,n): #optimized fom method which only uses the precomuted values instead of calling the phi method
    result = 0
    precomvalues = precom(n)
    for i in np.array(range(0,n)):
        helper = 1 
        for x in g:
            helper = helper * precomvalues[(i*x)%n]
        result = result + helper
    merit =  result/n-1
    if merit.imag < 10e-15:
        return merit.real
    return "Error, figure of merit has a complex part"

def fom_precom_time(g,n): #gives the process time for the optimized fom method
    start = time.process_time()
    fom = fom_precom(g,n)
    end = time.process_time()
    cputime = end - start
    print(fom,"   time: ", format(cputime))

#print(fom_precom([1, 282, 197, 377, 233, 55, 73, 263, 408, 46] , 1009))
fom_precom_time([1, 282, 197, 377, 233, 55, 73, 263, 408, 46] , 1009)