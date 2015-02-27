def ExpToPolish(exp):
    Priority = {'*':3, '/':3, '+':2, '-':2, '(':1}
    functions = ['+', '-', '*', '/']
    result = []
    operands = []
    for part in range(len(exp)):
        if exp[part].isdigit():
            if part+1 < len(exp) and exp[part+1].isdigit():
                result.append(exp[part])
                continue
            else:
                result.extend([exp[part], ' '])
        if exp[part] == ' ':
            continue
        if exp[part] in functions or exp[part] == '(':
            operands.append(exp[part])
        if exp[part] == ')':
            poper = operands.pop()
            while poper != '(':
                result.extend([poper, ' '])
                poper = operands.pop()
            while len(operands) > 0:
                if operands[-1] in functions:
                    result.extend([operands.pop(), ' '])
                else:
                    break
        if exp[part] in ['*', '/']:
            while len(operands) > 2 and Priority[exp[part]] <= Priority[operands[-1]]:
                result.extend([operands.pop(), ' '])

    while operands:
        result.extend([' ', operands.pop()])
    return ''.join(result)

def Polish(string):
    res = []
    string = string.split()
    for el in string:
        if el.isdigit():
            res.append(el)
        elif el in ['+','-','*','/']:
            try:
                y = res.pop()
                x = res.pop()
                res.append(str(eval(x+el+y)))
            except IndexError:
                print  'Error! Check input expression'
                break
            except ZeroDivisionError:
                print 'Error! Zero division!'
                break
    if len(res) !=1:
        return 'Error! Wrong numbers of operands'
    return res.pop()

if __name__ == '__main__':
    #string = '234 345 456 + + 5 /'
    #string = '8 2 5 * + 1 3 2 * + 4 - /'
    #print Polish(string)
    string = '3*(2+10)+5*10'
    pol = ExpToPolish(string)
    print pol
    print Polish(pol)