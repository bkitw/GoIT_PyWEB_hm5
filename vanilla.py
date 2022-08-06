
from time import time

def factorize(*number):
    result = []
    for i in number:
        subresult = []
        for n in range(1, i + 1):
            if i % n == 0:
                subresult.append(n)
        result.append(subresult)
    return result
    raise NotImplementedError()

if __name__ == "__main__":

    strt_time = time()
    print(f'Started at -- {time()}')
    a, b, c, d, = factorize(10000000, 20000000, 90000000, 30000000)
    # a, b, c, d = factorize(128, 255, 99999, 10651060)
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
    #          380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    fnsh_time = time()
    print(f'Finished at -- {time()}')
    passed = fnsh_time - strt_time
    print(f'Time passed -- {passed}')
    print("all done")

