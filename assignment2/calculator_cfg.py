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

    def divide(self, args):
        if args[1] == 0:
            raise ValueError("Division by zero")
        return args[0] / args[1]

    def power(self, args):
        return args[0] ** args[1]

    def negate(self, args):
        return -args[0]

    def number(self, args):
        return float(args[0])

    def scientific(self, args):
        return float(args[0])

    def logarithm(self, args):
        if args[0] <= 0 or args[1] <= 0 or args[1] == 1:
            raise ValueError("Invalid logarithm arguments")
        return math.log(args[0], args[1])

    def natural_log(self, args):
        if args[0] <= 0:
            raise ValueError("Invalid argument for natural logarithm")
        return math.log(args[0])

    def sine(self, args):
        return math.sin(args[0])

    def cosine(self, args):
        return math.cos(args[0])

    def tangent(self, args):
        return math.tan(args[0])

    def square_root(self, args):
        if args[0] < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(args[0])

    def absolute_value(self, args):
        return abs(args[0])

    def pi(self, args):
        return math.pi

    def e(self, args):
        return math.e

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