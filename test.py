import numpy as np
import math
from test import tools
import matplotlib.pyplot as plt

eta_vector = [1]*(7-1)
prevalues = tools.precom(5)
print(prevalues[4])
print(prevalues[4*1%5])
print(tools.omega_matrix(5))