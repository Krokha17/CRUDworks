def Opr(a,b,op): # �������, ������������ ��������� �������������� �������� � ����� �������.

    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b != 0:
            res = a / b
        else:
            res = 0

    return res # � ������ ������� ����� ���������� ������������ ���������� ��������

def RemWhitespase(s):
    p = ""
    i = 0
    while i < int( len(s) ):
        if (s[i] != ' ') and (s[i] != '\t') and (s[i] != '\n'):
            p += s[i]
        i += 1
    return p

s = input("enter the expression: ") 
fr = s # �������� �������� ������
s = RemWhitespase(s) # �������, ��������� ��� ������������ �������

oper = "" # ���������� �������� ���� �������������� ��������
num1 = "" 
num2 = ""
num3 = ""
i = 0 # ������� 
bracket = False

while i < int( len(s) ): # ���� ����������, ���� �� � ��������� ������
    if s[i] == '(' or s[i] == ')':
        bracket = True
        break
    i += 1

if bracket: # ���� ���� ������
    if s[0] == '(':
        i = 1

        while s[i] not in ['+', '-', '*', '/']: # ���� ���������� ������� �����
            num1 += s[i]
            i += 1
        oper = s[i] # ���������� ���� �������������� ��������
        i += 1
        while s[i] != ')': # ���� ���������� ������� �����
            num2 += s[i]
            i += 1
    
        num1 = float(num1) # ��������� ������ ����� � ����� � ��������� ������
        num2 = float(num2) #

        res = Opr(num1, num2, oper) # ��������� ��������� � �������

        i += 1
        oper = s[i] # ���������� ���� ���������. ����.
        i += 1

        while i < int( len(s) ): # ���� ���������� �������� �����
            num3 += s[i]
            i += 1
    
        res = Opr(res, float(num3), oper) #���������� �������� ����� � ����������� � �������
    else: # ���� ��������� ���������� � �����
        i = 0
        while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*':  # ���� ���������� ������� ����� 
            num1 += s[i]
            i += 1
        oper = s[i] # ���������� ���� ���������. ����.
        i += 1
        save = oper # ��� ��� ��������� � ������� ��� �� ����������, � ���� �������� ��� ��������, �� ��� ����� ��������� 
                    # ����� ������� ��� ���������� ��������

        if s[i] == '(':
            i += 1
            while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*': # ���� ���������� ������� �����
                num2 += s[i]
                i += 1
        
            oper = s[i] # ���������� ���� ���������. ����.
            i += 1

            while s[i] != ')': # ���� ���������� �������� �����
                num3 += s[i]
                i += 1
    
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)

        res = Opr(num2,num3, oper)
        res = Opr(num1, res, save)
else: #���� � ��������� ���� ������
    i = 0
    oper2 = ""

    while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*': # ���� ���������� ������� �����
        num1 += s[i]
        i += 1
    oper = s[i]
    i += 1
    while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*': # ���� ���������� ������� �����
        num2 += s[i]
        i += 1
    oper2 = s[i]
    i += 1
    while i < int( len(s) ): # ���� ���������� �������� �����
        num3 += s[i]
        i += 1
    
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)

    if (oper == '*' or oper == '/') and (oper2 == '+' or oper2 == '-'): #������� ���������� ����������� ��������
        res = Opr(num1, num2, oper)
        res = Opr(res, num3, oper2)
    elif (oper == '+' or oper == '-') and (oper2 == '*' or oper2 == '/'):
        res = Opr(num2, num3, oper2)
        res = Opr(num1, res, oper)
    else:
        res = Opr(num1, num2, oper)
        res = Opr(res, num3, oper2)
    
    
    

print(fr + " = " + str(res)) # ���������
        











