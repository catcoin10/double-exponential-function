import sys
from mpmath import *
mp.dps = 25
mult = mpf(sys.argv[2])
base = int(sys.argv[1]) / 1000
exp = int((10 ** 10 ** base) * mult)
print(exp)
