#!/usr/bn/python

import sys
import re

def check_power(eqn) :
    ans = re.findall("X\^([3-9]\d?|\d+\d)", eqn)
    if len(ans) != 0 :
        return ans[0]
    ans = re.findall("X\^([1-3])", eqn)
    ans.sort()
    if len(ans) != 0 :
        return ans[len(ans) - 1]
    ans = re.findall("X\^([0])", eqn)
    ans.sort()
    if len(ans) != 0 :
        return ans[len(ans) - 1]
    return len(ans)

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

def highest_power(eqn) :
    ans = re.findall("X\^([0-9]\d?|\d+\d)", eqn)
    high = 0
    for i in ans :
        i = i.replace(" ", "")
        if high < float(i) :
            high = float(i)
    print(high)
    return(high)


def solve(eqn) :
    power = highest_power(eqn)
    if power == 0:
        search = re.findall("((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^\d)", eqn)
        c = float(search[0][0].replace(" ", ""))
        if c == 0 :
            print ("The Solution is all real numbers")
        else :
            print("No real solution")
        # print("The solution is: \n" + str(c * -1))
    if power == 1:
        search = re.findall("((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^\d)", eqn)
        c = float(search[0][0].replace(" ", ""))
        b = float(search[1][0].replace(" ", ""))
        solution = (c * -1) / (b)
        print("Solution: " + str(solution))
    if power == 2:
        search = re.findall("((?:\+|\-)?(?: )?(\d?|\d+?.?\d+?))(?: \* X\^\d)", eqn)
        c = float(search[0][0].replace(" ", ""))
        b = float(search[1][0].replace(" ", ""))
        a = float(search[2][0].replace(" ", ""))
        if a == 0:
            print("Can't solve!")
            return(0)
        print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))
        if (b**2 - (4*a*c)) < 0 :
            print("Discriminant is strictly negative, the two solutions are:")
            solution = (-b - (b**2 - (4*a*c))**0.5)/(2 * a)
            print(str(solution))
            solution = (-b + (b**2 - (4*a*c))**0.5)/(2 * a)
            print(str(solution))
            return(0)
        print("Discriminant is strictly positive, the two solutions are:")
        solution = (-b - (b**2 - (4*a*c))**0.5)/(2 * a)
        print(str(solution))
        solution = (-b + (b**2 - (4*a*c))**0.5)/(2 * a)
        print(str(solution))

    

if len(sys.argv) == 2 :
    equation = sys.argv[1]
    equation = equation.upper()
    lhs = equation.split(" = ")[0].upper()
    rhs = equation.split(" = ")[1].upper()
    
    rhs_new = change_sign(rhs)
    equation = simplify(lhs + rhs_new)
    print("Reduced form: " + equation + " = 0")

    if float(check_power(equation)) >= 3 :
        print("Polynomial degree: " + check_power(equation))
        print("The polynomial degree is strictly greater than 2, I can't solve.")

    else :
        print("Polynomial degree: " + check_power(equation))
        ans = solve(equation)

else :
    print("No Arguments!")