def fibonacci(n):
    if n <= 1:
        return n
    else:
        a = fibonacci(n - 1)
        b = fibonacci(n-2)

        return (a + b)


num = int(input('Type a valid natural number: '))

while num < 1:
    num = int(input('Not a valid number. Please type a natural number greater than 1: '))

else:
    print(fibonacci(num))
