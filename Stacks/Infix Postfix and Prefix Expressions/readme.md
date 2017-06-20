# Infix Expressions
B * C 
*This type of notation is referred to as infix since the operator is in between the two operands that it is working on.*

### Points regarding **precedence** level
- Each operator has a precedence level. 
- Operators of higher precedence are used before operators of lower precedence. 
- The only thing that can change that order is the presence of parentheses. 
- If two operators of equal precedence appear, then a left-to-right ordering or associativity is used.

# Prefix Expressions
+ A B
Prefix expression notation requires that all operators precede the two operands that they work on. 

# Postfix Expression
A B +
Postfix, on the other hand, requires that its operators come after the corresponding operands. 

> The order of operations within prefix and postfix expressions is completely determined by the position of the operator and nothing else. 

Infix Expression | Prefix Expression | Postfix Expression
---------------- | ----------------- | ------------------
A + B | + A B | A B +
A + B * C | + A * B C | A B C * +
(A + B) * C | * + A B C | A B + C *

# Conversion of Infix Expressions to Prefix and Postfix

(A + (B * C))

- Prefix

![Prefix](http://interactivepython.org/runestone/static/pythonds/_images/moveleft.png)

- Postfix

![Postfix](http://interactivepython.org/runestone/static/pythonds/_images/moveright.png)

## Infix to Postfic Conversion

1. Create an empty stack called `opstack` for keeping operators. Create an empty list for output.
2. Convert the input infix string to a list by using the string method `split`.
3. Scan the token list from left to right.
    - If the token is an operand, append it to the end of the output list.
    - If the token is a left parenthesis, push it on the `opstack`.
    - If the token is a right parenthesis, pop the `opstack` until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
    - If the token is an operator, * , /, +, or -, push it on the `opstack`. However, first remove any operators already on the `opstack` that have higher or equal precedence and append them to the output list.
4. When the input expression has been completely processed, check the `opstack`. Any operators still on the stack can be removed and appended to the end of the output list.

![example](http://interactivepython.org/runestone/static/pythonds/_images/intopost.png)

## Postfix Evaluation
1. Create an empty stack called `operandStack`.
2. Convert the string to a list by using the string method `split`.
3. Scan the token list from left to right.
    - If the token is an operand, convert it from a string to an integer and push the value onto the `operandStack`.
    - If the token is an operator, * , /, +, or -, it will need two operands. Pop the `operandStack` twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the `operandStack`.
4. When the input expression has been completely processed, the result is on the stack. Pop the `operandStack` and return the value.



