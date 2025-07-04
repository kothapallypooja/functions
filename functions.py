def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))
a=int(input('enter a number: '))
result=factorial(a)
print('factorial of', a, 'is' , result)