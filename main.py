from opr import calc_binary_operation
from reme import reme
from search import SearchBracket
from calc1 import calculate
s = input("enter the expression: ")
fr = s
s = reme(s)
operations = ""
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
        operations = s[i]
        i += 1
        while s[i] != ')':
            num2 += s[i]
            i += 1
        num1 = float(num1)
        num2 = float(num2)

        result = calc_binary_operation(num1, num2, operations)

        i += 1
        operations = s[i]
        i += 1

        while i < int(len(s)):
            num3 += s[i]
            i += 1

        result = calc_binary_operation(result, float(num3), operations)
    else:
        i = 0
        while s[i] not in ['+', '-', '*', '/']:
            num1 += s[i]
            i += 1
        operations = s[i]
        i += 1
        save = operations

        if s[i] == '(':
            i += 1
            while s[i] not in ['+', '-', '*', '/']:
                num2 += s[i]
                i += 1

            operations = s[i]
            i += 1

            while s[i] != ')':
                num3 += s[i]
                i += 1

        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)

        result = calc_binary_operation(num2, num3, operations)
        result = calc_binary_operation(num1, result, save)
else:
     i = 0
     operations2 = ""

     while s[i] not in ['+', '-', '*', '/']:
      num1 = s[i]
      i += 1
     operations = s[i]
     i += 1
     while s[i] not in ['+', '-', '*', '/']:
        num2 += s[i]
        i += 1
     if i+1 < int (len (s) ):
      operations = s[i]
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

print(fr + " = " + str(result))











