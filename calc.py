def calc2(num1, num2, num3, operations, operations2):
    if (operations == '*' or operations == '/') and (operations2 == '+' or operations2 == '-'):
        result = calc_binary_operation(num1, num2, operations)
        result = calc_binary_operation(result, num3, operations2)
    elif (operations == '+' or operations == '-') and (operations2 == '*' or operations2 == '/'):
        result = calc_binary_operation(num2, num3, operations2)
        result = calc_binary_operation(num1, result, operations)
    else:
        result = calc_binary_operation(num1, num2, operations)
        result = calc_binary_operation(result, num3, operations2)
    return result
result = calc2(num1, num2, num3, operations, operations2)