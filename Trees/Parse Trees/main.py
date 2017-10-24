from Stacks.stack1 import Stack
from Trees.Tree_Structure_Using_Classes import BinaryTree
import operator


def build_parse_tree(funcExp):
    """
    An application of post-order traversal
    Build a parse tree
    Args:
        funcExp: function expression to build parse tree with
    Returns:
        A Binary tree
    """
    funcExp = funcExp.split()
    pStack = Stack()
    etree = BinaryTree('')
    pStack.push(etree)
    currentTree = etree

    for i in funcExp:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError

    return etree


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
        leftC = evaluate(parse_tree.getLeftChild())
        # evaluate right sub tree
        rightC = evaluate(parse_tree.getRightChild())
        # if left and right subtree exist, calculate and return
        # final result
        if leftC and rightC:
            fn = opers[parse_tree.getRootVal()]
            return fn(leftC, rightC)
        # return final result
        else:
            return parse_tree.getRootVal()


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
        sval = print_exp(parse_tree.getLeftChild())
        sval = sval + str(parse_tree.getRootVal())
        sval = sval + print_exp(parse_tree.getRightChild())
    return sval


pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))
print(print_exp(pt))
