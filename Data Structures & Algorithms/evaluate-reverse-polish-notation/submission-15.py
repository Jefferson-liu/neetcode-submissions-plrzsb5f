class Solution:
    

    def evalRPN(self, tokens: List[str]) -> int:
        def resolve(a,b,op):
            if op == '+':
                return a + b
            if op == '-':
                return b - a
            if op == '*':
                return b * a
            if op == '/':
                return int(b / a)

        # two operands, ab and the operator c
        # parse through, whenever we see a two operand pattern then we use the top operator
        # 1 2 + = 3
        # 1 2 4 + - = 4 - (1 + 2)
        ops = ['+', '-', '*', '/']
        operands = []
        operators = []
        for i in range(len(tokens)):
            if tokens[i] in ops:
                operators.append(tokens[i])
            else:
                operands.append(int(tokens[i]))
            
            # if the number of operands is equal to 1 + number of operators
            while len(operators) > 0:
                # resolve
                operator = operators.pop()
                a = operands.pop()
                if len(operators) == 0:
                    b = operands.pop()
                    operands.append(resolve(a,b,operator))
        return operands[0]


