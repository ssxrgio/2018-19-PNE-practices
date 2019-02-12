import math


def fibo_sum(n):  # I have used the formula F(n+2) - 1  deduced by induction.

    sum = (((1 + math.sqrt(5)) ** n) - ((1 - math.sqrt(5)) ** n)) / ((2 ** n) * math.sqrt(5))

    return int(sum - 1)


num = int(input('Type a valid integer number: '))

while num <= 1:
    print()
    print(num, 'is not a valid integer. Please try again with an integer greater than 1.')
    num = int(input('\nType a valid integer number: '))


else:
    print('\nThe sum of the first', num, 'integers of the Fibonacci sequence is', fibo_sum(num + 2), end='.')