import operator

prio = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv)
}

def eval_expr(expr):
    numbers = []
    operands = []
    number = 0
    i = 0

    def calculate():
        op2 = numbers.pop()
        op1 = numbers.pop()
        op = operands.pop()
        result = prio[op][1](op1, op2)
        numbers.append(result)
    
    while i < len(expr):
        char = expr[i]
        if char == ' ':
            i += 1
            continue
        if char.isdigit():
            number = 0
            while i < len(expr) and expr[i].isdigit():
                number = number * 10 + int(expr[i])
                i += 1
            numbers.append(number)
            continue
        elif char in prio:
            while (operands and prio[operands[-1]][0] >= prio[char][0]):
                calculate()
            operands.append(char)
        
        i += 1

    while operands:
        calculate()
    
    return numbers[0]

expr1 = "4+17-9*2+16/4"
expr2 = "121*2+15*6-20-21+4-3*4*2"
expr3 = "36/6+5*2-8-4-2*2*2+2"

result1 = eval_expr(expr1)
result2 = eval_expr(expr2)
result3 = eval_expr(expr3)

print(result1, result2, result3)
