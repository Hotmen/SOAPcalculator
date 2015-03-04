def exptopolish(exp):
    priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    functions = ['-', '+', '*', '/']
    result = []
    operands = []
    lastdigit = False
    if exp.strip()[-1] in functions or exp.strip()[0] in functions[1:]:
        return 'Error! Check input expression'
    for part in range(len(exp)):
        if exp[part] == '-' and len(result) == 0:
            result.append(exp[part])
            continue
        if exp[part].isdigit():
            if part+1 < len(exp) and exp[part+1].isdigit():
                result.append(exp[part])
                continue
            if lastdigit:
                return 'Error! Missed operator between numbers'
            result.extend([exp[part], ' '])
            lastdigit = True
            continue
        if exp[part] == ' ':
            continue
        if exp[part] == '(':
            operands.append(exp[part])
        if exp[part] in functions:
            if not operands or operands[-1] == '(':
                operands.append(exp[part])
            else:
                while len(operands) > 0 and priority[exp[part]] <= priority[operands[-1]]:
                    result.extend([operands.pop(), ' '])
                operands.append(exp[part])
        if exp[part] == ')':
            poper = operands.pop()
            while poper != '(':
                result.extend([poper, ' '])
                poper = operands.pop()
        lastdigit = False
    while operands:
        if result[-1] != ' ':
            result.extend([' ', operands.pop()])
        else:
            result.append(operands.pop())
    return ''.join(result)


def polish(string):
    res = []
    string = string.split()
    for el in string:
        if el.startswith('-') and len(el) > 1:
            res.append(el)
        elif el.isdigit():
            res.append(el)
        elif el in ['+', '-', '*', '/']:
            try:
                y = res.pop()
                x = res.pop()
                res.append(str(eval(x+el+y)))
            except IndexError:
                return 'Error! Wrong numbers of operands'
            except ZeroDivisionError:
                return 'Error! Zero division!'
    if len(res) != 1:
        return 'Error! Wrong numbers of operands'
    return int(res.pop())

if __name__ == '__main__':
    expression = '8 2 5 * + 1 3 2 * + 4 - / *'
    pol = exptopolish(expression)
    print pol
    print polish(pol)