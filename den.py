
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numba import prange, jit
import time as tm
from scipy.interpolate import griddata

TT = tm.time()         
def lrange(r1, inc, r2):
    """Matlabdaki " : " operatoru icin, scicomptan alinti"""
    n = ((r2-r1)+2*np.spacing(r2-r1))//inc
    return np.linspace(r1,r1+inc*n,n+1)
