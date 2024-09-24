from lark import Lark, Transformer
import sys
import math

# Load the grammar from the file
with open('grammar.lark', 'r') as grammar_file:
    grammar = grammar_file.read()

# Create the Lark parser
parser = Lark(grammar, start='exp', parser='lalr')

class CalculatorTransformer(Transformer):
    def add(self, args):
        return args[0] + args[1]

    def subtract(self, args):
        return args[0] - args[1]

    def multiply(self, args):
        return args[0] * args[1]

    def power(self, args):
        return args[0] ** args[1]

    def negate(self, args):
        return -args[0]

    def logarithm(self, args):
        return math.log(args[0], args[1])

    def number(self, args):
        return float(args[0])

def calculate(expression):
    try:
        # Parse the expression and evaluate it
        tree = parser.parse(expression)
        result = CalculatorTransformer().transform(tree)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expression = sys.argv[1]
        result = calculate(expression)
        print(result)
    else:
        print("Please provide an expression as a command-line argument.")