from opr import calc_binary_operation
from reme import reme
from search import SearchBracket

s = input("enter the expression: ")
fr = s
s = reme(s)
oper = ""
num1 = ""
num2 = ""
num3 = ""
i = 0

bracket = SearchBracket(s)

if bracket:
    if s[0] == '(':
        i = 1
        while s[i] not in ['+', '-', '*', '/']:
            num1 += s [i]
            i += 1
        oper = s[i]
        i += 1
        while s[i] != ')':
            num2 += s[i]
            i += 1
        num1 = float(num1)
        num2 = float(num2)

        result = calc_binary_operation(num1, num2, oper)

        i += 1
        oper = s[i]
        i += 1

        while i < int(len(s)):
            num3 += s[i]
            i += 1

        res = calc_binary_operation(result, float(num3), oper)
    else:
        i = 0
        while s[i] not in ['+', '-', '*', '/']:
            num1 += s[i]
            i += 1
        oper = s[i]
        i += 1
        save = oper

        if s[i] == '(':
            i += 1
            while s[i] not in ['+', '-', '*', '/']:
                num2 += s[i]
                i += 1

            oper = s[i]
            i += 1

            while s[i] != ')':
                num3 += s[i]
                i += 1

        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)

        res = calc_binary_operation(num2, num3, oper)
        res = calc_binary_operation(num1, res, save)
else:
     i = 0
     oper2 = ""

     while s[i] not in ['+', '-', '*', '/']:
      num1 = s[i]
      i += 1
     oper = s[i]
     i += 1
     while s[i] not in ['+', '-', '*', '/']:
        num2 += s[i]
        i += 1
     if i+1 < int (len (s) ):
      oper = s[i]
      i += 1
     while i < int(len(s)):
        num3 += s[i]
        i += 1
     if num1 != "":
         num1 = float(num1)
     else:
         num1 = 0
     if num2 != "":
         num2 = float(num2)
     else:
         num2 = 0
     if num3 != "":
       num3 = float(num3)
     else:
         num3 = 0


from calc import calc

print(fr + " = " + str(result))











