from Stacks.stack1 import Stack
import Balanced Parenthesis

def infix_to_postfix(infix_expr):
    # a dictionary to hold elements by precedence
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    opstack = Stack()
    postfixList = []
    tokenList = infix_expr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            top_token = opstack.pop()
            while top_token != "(":
                postfixList.append(top_token)
                top_token = opstack.pop()
        else:
            # before pushing an operator +,-,/,* to the stack
            # we should first remove any operators already in
            # the opstack that have higher or equal precedence
            # and append them to the output list
            while not opstack.isEmpty() and \
                    (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)

    # When the input expression has been completely processed,
    # check the opstack. Any operators still on the stack can
    # be removed and appended to the end of the output list.
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)


def validate(expr):
    """this function checks whetherthe input expression is validate or not"""
    # check for balanced parenthesis
    if not expr:
        return False
    s = []
    expr = expr.split()
    for e in expr:
        if e == '(' or e == ')':
            s.append(e)
    if not paren_checker(''.join(s)):
        return False

    # check for irrelevant values
    verified_list = []
    for e in expr:
        e = e.strip()
        verified_list.append(e)
        if e in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or "0123456789":
            continue
        elif e == '+' or e == '-' or e == '/' or e == '*':
            continue
        elif e == '(' or e == ')':
            continue
        else:
            return False
    # return verified list
    return " ".join(str(x) for x in verified_list)


def read_input():
    """read input from user"""
    print("Infix to Postfix")
    infix = input("Enter expression: ")
    temp = validate(infix)
    if temp:
        return temp
    else:
        return False


def main():
    """the executable function"""
    infix = read_input()
    if not infix:
        print("Invalid Expression!")
    else:
        print(infix_to_postfix(infix))


if __name__ == "__main__":
    main()
