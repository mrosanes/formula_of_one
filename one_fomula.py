#/usr/bin/env python

import sys
import math

import numpy

# formula_one:
# Summation[(-1)**i * n! * (n-i)**n / (i! * (n-i)!)] = 1

def formula_one(n):
    print(type(n))
    n = int(n)
    print(type(n))
    
    factorial_n = math.factorial(n)
    
    result = 0
    term = 0
    f_n = math.factorial(n)
    for i in range(n):
        f_i = math.factorial(i)
        f_n_min_i = math.factorial(n-i)
        term = (-1.0)**i * f_n * (n-i)**n / (f_i * f_n_min_i)
        result += term
        print(type(term))
        print(term)
    result = result / math.factorial(n)
    return result


if __name__ == "__main__":
    try: 
        result = formula_one(sys.argv[1])
        print("result:")
        print(result)
    except:
        msg = Exception("Code length (int) must be given as input argument")
        raise(msg)
        