from Stacks.stack1 import Stack

def infixToPostfix(infixexpr)
	# a dictionary to hold elements by precedence
	prec = {}
	prec["*"]=3
	prec["/"]=3
	prec["+"]=2
	prec["-"]=2
	prec["("]=1
	
	opstack=Stack()
	postfixList=[]
	tokenList=infixexpr.split()
	
	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == "(":
			opstack.push(token)
		elif token == ")":
			topToken = opstack.pop()
			while topToken != "(":
				postfixList.append(topToken)
				topToken=opstack.pop()
		else:
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
	
print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
