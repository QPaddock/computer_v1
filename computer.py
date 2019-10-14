#!/usr/bn/python

import sys
import re

if len(sys.argv) == 2 :
    equation = sys.argv[1]
    equation.upper()
    lhs = equation.split(" = ")[0].upper()
    rhs = equation.split(" = ")[1]
    print(lhs)
    print(rhs)

    search = re.findall("((?:\+|-)?(?: )?\d?|\d+?.?\d+?)(?: \* X\^2)", lhs)
    print(search)

else :
    print("No Arguments!")  