#!/usr/bn/python

import sys
import re

def check_power(eqn) :
    ans = re.findall("X\^([3-9]\d?|\d+\d)", eqn)
    if len(ans) != 0 :
        return ans[0]
    else :
        ans = re.findall("X\^([2])", eqn)
        return ans[len(ans) - 1]

def simplify(eqn) :
    i = 0
    j = 0
    new = ""
    arr_ans = []
    for i in range(int(check_power(eqn)) + 1) :
        ans = 0
        regex = "((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^" + str(i) + ")"
        eq_seg = re.findall(regex , eqn)
        if len(eq_seg) >= 2 :
            for k in eq_seg :
                ans += float(k[0].replace(" ", ""))
            ans = str(ans)
            if float(ans) >= 0 and i > 0 :
                ans = "+ " + ans
            ans = ans.replace(".0", "")
            ans = ans.replace("-", "- ")
            arr_ans.append(ans)
        else :
            for k in eq_seg :
                arr_ans.append(k[0])
    for i in arr_ans :
        new = new + i + " * X^" + str(j) + " "
        j += 1
    return(new)
 
def change_sign(eqn) :
    search = re.findall("((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^\d)", eqn)
    search_neg = [str(float(i[0].replace(" ", "")) * -1) for i in search]
    j = 0
    rhs = ""
    for i in search_neg :
        if float(i) >= 0 :
            i = "+ " + i
        i = i.replace(".0", "")
        i = i.replace("-", "- ")
        add = i + " * X^" + str(j)
        rhs = rhs + " " + add
        j += 1
    return rhs

def solve(eqn) :
    search = re.findall("((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^\d)", eqn)
    c = float(search[0][0].replace(" ", ""))
    b = float(search[1][0].replace(" ", ""))
    a = float(search[2][0].replace(" ", ""))
    print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))

    

if len(sys.argv) == 2 :
    equation = sys.argv[1]
    equation = equation.upper()
    lhs = equation.split(" = ")[0].upper()
    rhs = equation.split(" = ")[1].upper()
    print(lhs)
    print(rhs)
    
    rhs_new = change_sign(rhs)
    equation = simplify(lhs + rhs_new)
    print("Reduced form: " + equation + " = 0")

    if float(check_power(equation)) >= 3 :
        print("Polynomial degree: " + check_power(equation))

    else : 
        print("im here")
        print("Polynomial degree: " + check_power(equation))
        ans = solve(equation)

else :
    print("No Arguments!")  