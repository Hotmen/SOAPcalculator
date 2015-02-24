Priority = {'*':3, '/':3, '+':2, '-':2, '(':1}
functions = ['+', '-', '*', '/']

def ExpToPolish(expression):
    expression = expression.split()
    result = []
    operands = []
    for part in expression:
        if part.isdigit():
            result.append(part)
            continue
        #if not operands:
        #    operands.append(part)
        if part in functions or part == '(':
            operands.append(part)
        if part == ')':
            poper = operands.pop()
            while poper != '(':
                result.append(poper)
                poper = operands.pop()
            #operands.pop()
            while len(operands) > 0:
                if operands[-1] in functions:
                    result.append(operands.pop())
                else:
                    break
        if part in ['*', '/']:
            while len(operands) > 2 and Priority[part] <= Priority[operands[-1]]:
                result.append(operands.pop())

    while operands:
        result.append(operands.pop())
    return ' '.join(result)

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
                print 'Error! Zero divizion!'
                break
    if len(res) !=1:
        return 'Error! Wrong numbers of operands'
    return res.pop()

if __name__ == '__main__':
    #string = '234 345 456 + + 5 /'
    #string = '8 2 5 * + 1 3 2 * + 4 - /'
    #print Polish(string)
    string = '3 * ( 2 + 1 ) + 5 * 10'
    print ExpToPolish(string)
