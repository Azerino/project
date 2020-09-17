import numpy as np
import math
from test import tools

def fastcbc(n,s):   #algorithm 4.8
    omega_n = tools.mat(n)
    phi_n = tools.precom(n)  #1 TODO: implement FFT to speed up computation
    eta_vector = [1]*(n-1)   #2
    #3:
    for d in range(1,s):
        #i)






