def reverse(str):
	if len(str) == 1:
		return str[-1:]
	else:
		return str[-1:] + reverse(str[0:len(str)-1])
