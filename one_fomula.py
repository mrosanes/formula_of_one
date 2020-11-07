#/usr/bin/env python

###############################################################################
# Copyright one_formula.py script - 2020 Marc Rosanes Siscart 
# Copyright of the formula_of_one discovered - May 2014 Marc Rosanes Siscart
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# GNU General Public License on: <https://www.gnu.org/licenses/>.
###############################################################################


import sys   
import math


# Formula of One by Marc Rosanes Siscart:
# summation[(-1)**i * (n-i)**n / (i! * (n-i)!)] = 1
#
# Note: Summation can be done 'between 0 and n-1', or 'between 0 and n'; 
# it is indiferent.

def formula_one(n):
    n = int(n)
    term = 0
    result = 0
    factorial_n = math.factorial(n)  
    f_n = math.factorial(n)
    for i in range(n):
        f_i = math.factorial(i)
        f_n_min_i = math.factorial(n-i)
        term = (-1.0)**i * (n-i)**n / (f_i * f_n_min_i)
        result += term
    return result


if __name__ == "__main__":
    try:
        result = formula_one(sys.argv[1])
        print("result= " + str(result))
    except:
        msg = Exception("Code length (int) must be given as input argument")
        raise(msg)
