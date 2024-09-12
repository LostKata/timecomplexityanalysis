import time # time.time_ns
# from time import time_ns
from binsearch import binsearch; from linsearch import linsearch

start_ns = time.time_ns()
i = linsearch(list(range(100000)), 66666)
end_ns = time.time_ns()
dt_ns = (end_ns - start_ns)/1000000
print(i)
print("elapsed time ms", dt_ns)
# print(start_ns, end_ns)