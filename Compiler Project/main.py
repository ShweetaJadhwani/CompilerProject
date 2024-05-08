# Operator Precedence Parser
def operator_precedence_parser(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token in operators:
            while (
                operator_stack and
                operator_stack[-1] in operators and
                operators[operator_stack[-1]] >= operators[token]
            ):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
            else:
                raise ValueError("Mismatched parentheses")
        else:
            raise ValueError("Invalid token: " + token)

    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(operator_stack.pop())

    return evaluate_postfix(output)

def evaluate_postfix(postfix):
    operand_stack = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    for token in postfix:
        if token.isnumeric():
            operand_stack.append(int(token))
        elif token in operators:
            if len(operand_stack) < 2:
                raise ValueError("Invalid expression")
            b = operand_stack.pop()
            a = operand_stack.pop()
            if token == '+':
                operand_stack.append(a + b)
            elif token == '-':
                operand_stack.append(a - b)
            elif token == '*':
                operand_stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                operand_stack.append(a / b)
    if len(operand_stack) != 1:
        raise ValueError("Invalid expression")
    return operand_stack[0]

def main():
    expression = input("Enter an arithmetic expression: ")
    try:
        result = operator_precedence_parser(expression)
        print("Result:", result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()