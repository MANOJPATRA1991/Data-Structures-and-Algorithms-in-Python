def get_fib(position):
    fib = [0,1]
    for i in range(2, position+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[position]
