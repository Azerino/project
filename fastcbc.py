import numpy as np
import math
from test import generatorp as gp
from test import tools

def cbc(n,s):   #algorithm 4.8 without FFT
    genereating_vector = [1]*s
    omega_n = tools.omega_matrix(n)
    phi_n = tools.precom(n)  #1 
    eta_vector = [1]*(n-1)   #2
    #3:
    for d in range(1,s):
        T_n = np.matmul(omega_n,eta_vector)      #i) 
        #print(T_n)
        genereating_vector[d-1] = np.argmin(T_n)+1 #ii)
        for i in range(0,n-1):                   #iii)
            eta_vector[i] = eta_vector[i] * phi_n[(i*genereating_vector[d-1])%n] #holds
    return genereating_vector    


def fastcbc(n,s):   #algorithm 4.8 with FFT
    generating_vector = [1]*s
    omega_n = tools.omega_matrix_c(n)
    phi_n = tools.getphi_n(n)  #1 
    q = gp.generatorp(n)
    diagvec = tools.getdiagmatrixasvector(q,n,phi_n)
    permmat = tools.getpermmatrix(q,n)
    permmatinv = tools.getpermmatrix(gp.pinverse(q,n),n)
    eta_vector = [1]*(n-1)   #2
    #3:
    for d in range(1,s):
        first = np.matmul(np.transpose(permmatinv),eta_vector)
        second = np.fft.fft(first)
        third = np.multiply(diagvec,second)
        fourth = np.fft.ifft(third)
        T_n = np.matmul(np.transpose(permmat),fourth)      #i) TODO: Fix Errors
        generating_vector[d-1] = np.argmin(T_n)+1 #ii)
        for i in range(0,n-1):                   #iii)
            eta_vector[i] = eta_vector[i] * phi_n[(i*generating_vector[d-1])%n] 
    return generating_vector    

