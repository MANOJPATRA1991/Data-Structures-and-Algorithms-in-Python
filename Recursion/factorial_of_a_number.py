def factorial(num):

  # This is the most efficient base case as it keeps our program from crashing 
  # if you try to compute the factorial of a negative number.
	if num <= 1:
		return 1
	else:
		return num * factorial(num-1)

	
