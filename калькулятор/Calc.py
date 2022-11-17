def Opr(a,b,op): # функция, возвращающая результат арифметической операции и флаги ошибкок.

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

    return res # в питоне функции умеют возвращать произвольное количество значений

def RemWhitespase(s):
    p = ""
    i = 0
    while i < int( len(s) ):
        if (s[i] != ' ') and (s[i] != '\t') and (s[i] != '\n'):
            p += s[i]
        i += 1
    return p

s = input("enter the expression: ") 
fr = s # копируем введеную строку
s = RemWhitespase(s) # функция, удаляющая все непечатаемые символы

oper = "" # переменная хранящая знак арфиметической операции
num1 = "" 
num2 = ""
num3 = ""
i = 0 # счетчик 
bracket = False

while i < int( len(s) ): # цикл определяет, если ли в выражении скобки
    if s[i] == '(' or s[i] == ')':
        bracket = True
        break
    i += 1

if bracket: # если есть скобки
    if s[0] == '(':
        i = 1

        while s[i] not in ['+', '-', '*', '/']: # цикл вычисления первого числа
            num1 += s[i]
            i += 1
        oper = s[i] # запоминаем знак арифметической операции
        i += 1
        while s[i] != ')': # цикл вычисления второго числа
            num2 += s[i]
            i += 1
    
        num1 = float(num1) # переводим строку чисел в число с плавающей точкой
        num2 = float(num2) #

        res = Opr(num1, num2, oper) # вычисляем выражение в скобках

        i += 1
        oper = s[i] # запоминаем знак арифметич. опер.
        i += 1

        while i < int( len(s) ): # цикл вычисления третьего числа
            num3 += s[i]
            i += 1
    
        res = Opr(res, float(num3), oper) #вычисление трерьего числа с результатом в скобках
    else: # если выражение начинается с числа
        i = 0
        while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*':  # цикл вычисления первого числа 
            num1 += s[i]
            i += 1
        oper = s[i] # запоминаем знак арифметич. опер.
        i += 1
        save = oper # так как выражение в скобках еще не определено, а знак операции уже известен, то его нужно сохранить 
                    # иначе получим две одинаковые операции

        if s[i] == '(':
            i += 1
            while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*': # цикл вычисления второго числа
                num2 += s[i]
                i += 1
        
            oper = s[i] # запоминаем знак арифметич. опер.
            i += 1

            while s[i] != ')': # цикл вычисления третьего числа
                num3 += s[i]
                i += 1
    
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)

        res = Opr(num2,num3, oper)
        res = Opr(num1, res, save)
else: #если в выражении нету скобок
    i = 0
    oper2 = ""

    while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*': # цикл вычисления первого числа
        num1 += s[i]
        i += 1
    oper = s[i]
    i += 1
    while s[i] != '+' and s[i] != '-' and s[i] != '/' and s[i] != '*': # цикл вычисления второго числа
        num2 += s[i]
        i += 1
    oper2 = s[i]
    i += 1
    while i < int( len(s) ): # цикл вычисления третьего числа
        num3 += s[i]
        i += 1
    
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)

    if (oper == '*' or oper == '/') and (oper2 == '+' or oper2 == '-'): #условия вычисления приоритетов операции
        res = Opr(num1, num2, oper)
        res = Opr(res, num3, oper2)
    elif (oper == '+' or oper == '-') and (oper2 == '*' or oper2 == '/'):
        res = Opr(num2, num3, oper2)
        res = Opr(num1, res, oper)
    else:
        res = Opr(num1, num2, oper)
        res = Opr(res, num3, oper2)
    
    
    

print(fr + " = " + str(res)) # результат
        











