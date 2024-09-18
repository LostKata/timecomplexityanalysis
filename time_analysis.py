import time # time.time_ns()
import random
# from time import time_ns # time_ns()

import linsearch,  binsearch

for n in [1e4,5e4,1e5,5e5,1e6,3e6,6e6,1e7,3e7,5e7]:
    n = int(n)
    L = list(range(n))
    repeats = 100000
    total_time_ns = 0
    for _ in range(repeats): # Multiple runs for averaging
        r = random.choice(L)

        start_ns = time.time_ns()
        i = binsearch.binsearch(L, r)
        #i = linsearch.linsearch(L, r)
        end_ns = time.time_ns()

        dt_ns = end_ns - start_ns
        total_time_ns += dt_ns
    print(n, total_time_ns/repeats)

