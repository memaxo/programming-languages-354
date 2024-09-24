# Assignment 1 Specifications

## parentheses.py

### Function: is_balanced(s: str) -> bool

Purpose: Determines if a given string has balanced parentheses.

Logic:
1. Initialize an empty stack.
2. Iterate through each character in the input string:
   - If the character is an opening parenthesis '(', push it onto the stack.
   - If the character is a closing parenthesis ')':
     - If the stack is empty, return False (unbalanced).
     - Otherwise, pop the top element from the stack.
3. After iterating, if the stack is empty, return True (balanced). Otherwise, return False.

### Main execution:
1. Read the input string from command-line argument.
2. Call is_balanced() function with the input string.
3. Print "yes" if balanced, "no" if not.

## calculator.py

### Function: tokenize(expression: str) -> list

Purpose: Converts the input string into a list of tokens (numbers and operators).

Logic:
1. Initialize an empty list for tokens and an empty string for the current number.
2. Iterate through each character in the expression:
   - If the character is a digit, add it to the current number.
   - If it's an operator or parenthesis:
     - If there's a current number, convert it to an integer and add to tokens.
     - Add the operator or parenthesis to tokens.
3. If there's a remaining number after the loop, add it to tokens.
4. Return the list of tokens.

### Function: apply_operator(operators, values)

Purpose: Applies the top operator to the top two values in their respective stacks.

Logic:
1. Pop the top operator and the top two values.
2. Perform the operation based on the operator.
3. Push the result back onto the values stack.

### Function: evaluate(tokens: list) -> int

Purpose: Evaluates the expression represented by the list of tokens.

Logic:
1. Initialize empty stacks for values and operators.
2. Define operator precedence.
3. Iterate through each token:
   - If it's a number, push to values stack.
   - If it's an opening parenthesis, push to operators stack.
   - If it's a closing parenthesis, apply operators until opening parenthesis is found.
   - If it's an operator:
     - Apply operators of higher or equal precedence.
     - Push the current operator to the operators stack.
4. Apply any remaining operators.
5. Return the final value in the values stack.

### Main execution:
1. Read the expression from command-line argument.
2. Tokenize the expression.
3. Evaluate the tokens.
4. Print the result.