import numpy as np
import math
from test import tools
from test import generatorp as gp
import matplotlib.pyplot as plt
import fastcbc



n=7
perm = np.zeros(n-1, dtype=int)
perm[0] = 1
for i in np.arange(1, n-1):
    perm[i] = (perm[i-1]*3) % n
print(perm)

perminv = np.zeros(n-1, dtype=int)
for i in np.arange(1, n):
    perminv[perm[i-1]-1]= i
print(perminv)