from Stacks.stack1 import Stack


def postfix_eval(postfixexpr):
    op_stack = Stack()
    token_list = postfixexpr.split()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(int(token))
        else:
            # if op_stack's size is 1 then do_math can't
            # operate as it requires two operands
            if op_stack.size() < 2:
                return None
            operand2 = op_stack.pop()
            operand1 = op_stack.pop()
            result = do_math(token, operand1, operand2)
            op_stack.push(result)
    # if op_-stack size is greater than 1
    # then expression is missing an operator
    if op_stack.size() > 1:
        return None
    else:
        return op_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "^":
        return op1 ** op2
    # if operator other than -,+,*,/,^
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
