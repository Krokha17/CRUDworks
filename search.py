def SearchBracket(s):
    bracket = False
    i = 0
    while i < int (len (s) ):
        if s[i] == '(' or s[i] == ')':
            bracket = True
            break
        i += 1
    return bracket
