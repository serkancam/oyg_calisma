# %% recusrive fibonacci


# %% dynamic fibonacci
from functools import wraps
import time

def timeit(my_func):
    @wraps(my_func)
    def timed(*args, **kw):
    
        tstart = time.time()
        output = my_func(*args, **kw)
        tend = time.time()
        
        print('"{}" took {:.3f} ms to execute\n'.format(my_func.__name__, (tend - tstart) * 1000))
        return output
    return timed

@timeit
def d_fib(n, mem: dict = {}):
    if n in mem:
        return mem[n]
    if n <= 2:
        return 1

    mem[n] = d_fib(n-1, mem) + d_fib(n-2, mem)
    return mem[n]


print(d_fib(500))
# %%

@timeit
def fib(n):
    if n <= 2:
        return 1
    f1 = f2 = 1
    for _ in range(3, n+1):
        f1, f2 = f2, f1+f2
    return f2


print(fib(100000))
# %%
