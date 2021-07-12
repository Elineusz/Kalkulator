from functools import lru_cache

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    try:
        return a / b
    except:
        print('Nie dzieli się przez 0')
        return None
def power(x, p):
    return x ** p

@lru_cache(maxsize=None)
def factorial(n):
    if n > 1000:
        print('Podaj mniejszą liczbę')
        return None
    if n == 1:
        return 1
    return n*factorial(n-1)

symbol_to_func = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '!': factorial
}