from Stacks.stack1 import Stack
import Stacks.Balanced_Parenthesis.balanced_parenthesis as parenthesis
import Stacks.Infix_Postfix_and_Prefix_Expressions.postfix_evaluation as in_to_post

def infix_to_postfix(infix_expr):
    # a dictionary to hold elements by precedence
    prec = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    op_stack = Stack()
    char_stack = Stack()
    token_list = infix_expr.split()

    for token in token_list:
        if token in "0123456789":
            char_stack.push(int(token))
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                op2 = char_stack.pop()
                op1 = char_stack.pop()
                result = in_to_post.do_math(top_token, op1, op2)
                char_stack.push(result)
                top_token = op_stack.pop()
        else:
            # before pushing an operator +,-,/,* to the stack
            # we should first remove any operators already in
            # the op_stack that have higher or equal precedence
            # and append them to the output list
            while not op_stack.isEmpty() and (prec[op_stack.peek()] >= prec[token]):
                top_token = op_stack.pop()
                op2 = char_stack.pop()
                op1 = char_stack.pop()
                result = in_to_post.do_math(top_token, op1, op2)
                char_stack.push(result)
            op_stack.push(token)

    # When the input expression has been completely processed,
    # check the op_stack. Any operators still on the stack can
    # be removed and appended to the end of the output list.
    while not op_stack.isEmpty() and not char_stack.isEmpty():
        top_token = op_stack.pop()
        op2 = char_stack.pop()
        op1 = char_stack.pop()
        result = in_to_post.do_math(top_token, op1, op2)
        char_stack.push(result)

    return char_stack.pop()


def validate(expr):
    """this function checks whether the input expression is validate or not"""
    # check for balanced parenthesis
    if not expr:
        return False
    s = []
    expr = expr.split()
    for e in expr:
        if e == '(' or e == ')':
            s.append(e)
    if not parenthesis.paren_checker(''.join(s)):
        return False

    # check for irrelevant values
    verified_list = []
    for e in expr:
        e = e.strip()
        verified_list.append(e)
        if e in "0123456789":
            continue
        elif e == '+' or e == '-' or e == '/' or e == '*' or e == '^':
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
