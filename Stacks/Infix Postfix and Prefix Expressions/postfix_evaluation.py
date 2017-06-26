from Stacks.stack1 import Stack

def postfix_eval(postfixexpr):
    opStack = Stack()
    tokenList = postfixexpr.split()

    for token in tokenList:
        if token in "0123456789":
            opStack.push(int(token))
        else:
            # if opstack's size is 1 then do_math can't
            # operate as it requires two operands
            if opStack.size() < 2:
                return None
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            result = do_math(token, operand1, operand2)
            opStack.push(result)
    # if opstack size is greater than 1
    # then expression is missing an operator
    if opStack.size() > 1:
        return None
    else:
        return opStack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    # if operator other than -,+,*,/
    # return None
    else:
        return None


def read_input():
    print("Enter postfix expression separated by space.")
    inp = input("Expression: ")
    return inp


def main():
    postfix = read_input()
    result = postfix_eval(postfix)
    print("Result: ", result)


if __name__ == '__main__':
    main()

