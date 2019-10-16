#!/usr/bn/python

import sys
import re

def check_power(eqn) :
    ans = re.findall("X\^([3-9]\d?|\d+\d)", eqn)
    if len(ans) != 0 :
        return ans[0]
    else :
        return 0

def change_sign(eqn) :
    search = re.findall("((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^\d)", eqn)
    print(search)
    search_neg = [str(float(i[0].replace(" ", "")) * -1) for i in search]
    print(search_neg)
    j = 0
    rhs = ""
    for i in search_neg :
        i = i.replace(".0", "")
        i = i.replace("", " ")
        add = i + " * X^" + str(j)
        rhs = rhs + " " + add
        j += 1
        print(rhs)
    return search_neg

if len(sys.argv) == 2 :
    equation = sys.argv[1]
    equation.upper()
    lhs = equation.split(" = ")[0].upper()
    rhs = equation.split(" = ")[1].upper()
    print(lhs)
    print(rhs)
    
    rhs_new = change_sign(rhs)

    if check_power(equation) != 0 :
        print("Polynomial degree: " + check_power(equation))

    else : 
        search = re.findall("((?:\+|-)?(?: )?\d?|\d+?.?\d+?)(?: \* X\^1)", lhs)
        print(search)

else :
    print("No Arguments!")  