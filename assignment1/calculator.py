import sys

def tokenize(expression: str) -> list:
    # convert expression string to list of tokens
    tokens = []
    current_number = ''
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                tokens.append(int(current_number))
                current_number = ''
            if char in '+-*^()':
                tokens.append(char)
    if current_number:
        tokens.append(int(current_number))
    return tokens

def apply_operator(operators, values):
    # apply the top operator to the top two values
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '^':
        values.append(left ** right)

def evaluate(tokens: list) -> int:
    # evaluate the expression using shunting yard algorithm
    precedence = {'+': 1, '*': 2, '^': 3}
    values = []
    operators = []
    
    for token in tokens:
        if isinstance(token, int):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # remove '('
        else:  # operator
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence[token]):
                apply_operator(operators, values)
            operators.append(token)
    
    while operators:
        apply_operator(operators, values)
    
    return values[0]

if __name__ == "__main__":
    # get expression from command line argument
    expression = sys.argv[1]
    tokens = tokenize(expression)
    result = evaluate(tokens)
    print(result)