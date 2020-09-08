import re
from itertools import permutations
def solution(expression):
    #num_parser = re.compile('\d+')
    #op_parser = re.compile('\D')
    parser = re.compile('\d+|\D')
    cases = list(permutations(['-', '*', '+']))
    #numbers = num_parser.findall(expression)
    expr = parser.findall(expression)
    temp = expr
    result = []
    for case in cases:
        expr = temp
        for cur_op in case:
            idx = 0
            stack = []
            while True:
                if idx == len(expr): break
                if expr[idx] == cur_op:
                    calc = eval(str(stack.pop()) + str(cur_op) + str(expr[idx+1]))
                    idx += 2
                    stack.append(calc)
                    #print(calc)
                else:
                    stack.append(expr[idx])
                    idx += 1
            expr = stack
        result.append(abs(stack[0]))
    
    result.sort(reverse=True)
                
    return result[0]