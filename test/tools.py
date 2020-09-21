import numpy as np
import math
import time

def c(n):
    return np.array(range(int(-n/2),int(n/2+1)))

def r1(h):
    return max(1,abs(h))

def phi(x,n):   #book version: p. 78  , O(n)
    result = 0
    for h in c(n):
        result = result + ((1/r1(h))*np.exp(2*math.pi*complex(0,1)*h*x))
    return result

def precom(n): #precomputes the possible values for phi
    precomvalues = [0]*n
    for i in range(0,n):
        precomvalues[i] = phi(i/n,n)
    return np.array(precomvalues)

def mat(n):  #creates the matrix Omega_n according to the paper
    prevalues = precom(n)
    matrix = np.zeros(shape=(n-1,n))
    for i in range(1,n):
        for j in range(0,n):
            matrix[i-1,j]= prevalues[(i*j)%n].real
    return matrix

def omega_matrix(n):  #creates the matrix Omega_n according to the book
    prevalues = precom(n)
    matrix = np.zeros(shape=(n-1,n-1))
    for i in range(1,n):
        for j in range(1,n):
            matrix[i-1,j-1]= prevalues[(i*j)%n].real
    return matrix

def eta(vector,s,i,n,nmax,precomvalues="null"): #book p. 80 eta_d-1(n)
    if s == 0:
        return 1

    if precomvalues == "null":
        result = 1
        for j in range(1,s+1):
            result = result * phi(vector[j]*i/n)
        return result

    for j in range(1,s+1):
        result = result * precomvalues[(i*vector[j])%n]
    return result

def primfaktoren(n):
    """
    die Primfaktoren von n werden als Liste zurÃ¼ckgegeben
    """
    f = []
    while n%2 == 0:
        f = f + [2]
        n = n//2
    while n%3 == 0:
        f = f + [3]
        n = n//3
    t = 5
    diff = 2
    w = round(math.sqrt(n))
    while t <= w:
        while n%t == 0:
            f = f + [t]
            n = n//t
        t = t + diff
        diff = 6 - diff
    if n > 1:
        f = f + [n]
    return f
"""
Die Methode zur Primitivwurzel übernommen von: https://stackoverflow.com/questions/40190849/efficient-finding-primitive-roots-modulo-n-using-python
"""
def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if math.gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo) for powers in range(1, modulo)}]

def fourier_mat(m):
    fmat = np.zeros(shape=(m,m))
    omega = np.exp(2*math.pi*complex(0,1)/m)
    for k in range(0,m-1):
        for l in range(0,m-1):
            fmat[k,l]= np.power(np.power(omega, k*l),m-1)/np.sqrt(m)
    return fmat
