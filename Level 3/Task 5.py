#Generator Sequence
def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a + b
fib_sequence = list(fib(5))
print(fib_sequence)