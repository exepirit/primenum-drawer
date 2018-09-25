from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def isPrime1(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False