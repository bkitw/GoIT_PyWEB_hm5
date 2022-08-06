import vanilla as vanilla
import thread as thread
import processes as processes
from time import time


if __name__ == "__main__":
    print('Vanilla started:')
    strt_time = time()
    print(f'Started at -- {time()}')
    a, b, c, d, = vanilla.factorize(10000000, 20000000, 90000000, 30000000)
    fnsh_time = time()
    print(f'Finished at -- {time()}')
    passed = fnsh_time - strt_time
    print(f'Time passed -- {passed}')
    print("all done")
    ...
    print('Thread started:')
    strt_time = time()
    print(f'Started at -- {time()}')
    e, f, g, h, = thread.factorize(10000000, 20000000, 90000000, 30000000)
    fnsh_time = time()
    print(f'Finished at -- {time()}')
    passed = fnsh_time - strt_time
    print(f'Time passed -- {passed}')
    print("all done")
    ...
    print('Processes started:')
    strt_time = time()
    print(f'Started at -- {time()}')
    j, k, l, m, = processes.factorize(10000000, 20000000, 90000000, 30000000)
    fnsh_time = time()
    print(f'Finished at -- {time()}')
    passed = fnsh_time - strt_time
    print(f'Time passed -- {passed}')
    print("all done")
