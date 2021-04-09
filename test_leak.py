import os, psutil
from req import IntRequest

def create_lots_of_intrequests(n):
    rs = [IntRequest(42, 0) for _ in range(n)]
    return rs

process = psutil.Process(os.getpid())
origmem=process.memory_info().rss / 1024

xxx = create_lots_of_intrequests(2*10**8)
del xxx
print(process.memory_info().rss / 1024 - origmem)
xxx = create_lots_of_intrequests(2*10**8)
del xxx
print(process.memory_info().rss / 1024 - origmem)

