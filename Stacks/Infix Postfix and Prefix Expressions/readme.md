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



