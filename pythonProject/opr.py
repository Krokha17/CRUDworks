def calc_binary_operation(a, b, operation):
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a / b if b != 0 else 0
    return 0
