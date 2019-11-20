from Stacks.stack1 import Stack
from Trees.Tree_Structure_Using_Classes import BinaryTree
import operator


def build_parse_tree(func_exp):
    """
    An application of post-order traversal
    Build a parse tree
    Args:
        func_exp: function expression to build parse tree with
    Returns:
        A Binary tree
    """
    func_exp = func_exp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree

    for i in func_exp:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_val(int(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.getRightChild()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError

    return e_tree


def evaluate(parse_tree):
    """
    Evaluate the parse tree using post order traversal
    Args:
        parse_tree: Parse tree to evaluate
    Returns:
        Result of expression in parse tree
    """
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}

    leftC = None
    rightC = None

    if parse_tree:
        # evaluate left sub tree
        leftC = evaluate(parse_tree.get_left_child())
        # evaluate right sub tree
        rightC = evaluate(parse_tree.get_right_child())
        # if left and right subtree exist, calculate and return
        # final result
        if leftC and rightC:
            fn = opers[parse_tree.get_root_val()]
            return fn(leftC, rightC)
        # return final result
        else:
            return parse_tree.get_root_val()


def print_exp(parse_tree):
    """
    Prints the expression stored in parse tree
    Args:
        parse_tree: Parse tree expression to print
    Returns:
        Expression in parse tree
    """
    sval = ""
    if parse_tree:
        sval = print_exp(parse_tree.get_left_child())
        sval = sval + str(parse_tree.get_root_val())
        sval = sval + print_exp(parse_tree.get_right_child())
    return sval


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))
print(print_exp(pt))
