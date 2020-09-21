import numpy as np
import math
from test import tools

def fastcbc(n,s):   #algorithm 4.8
    genereating_vector = [0]*s
    omega_n = tools.omega_matrix(n)
    phi_n = tools.precom(n)  #1 TODO: implement FFT to speed up computation
    eta_vector = [1]*(n-1)   #2
    #3:
    for d in range(1,s):
        T_n = np.matmul(omega_n,eta_vector)      #i) TODO: FFT
        genereating_vector[d-1] = np.argmin(T_n) #ii)
        for i in range(0,n-1):                   #iii)
            eta_vector[i] = eta_vector[i] * phi_n[(i*genereating_vector[d-1])%n] 
    return genereating_vector    

print(fastcbc(1009, 10))






