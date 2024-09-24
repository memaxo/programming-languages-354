def is_balanced(s: str) -> bool:
    # stack to keep track of opening parentheses
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    # check if all parentheses are matched
    return len(stack) == 0

if __name__ == "__main__":
    import sys
    # get input string from command line argument
    input_string = sys.argv[1]
    print("yes" if is_balanced(input_string) else "no")