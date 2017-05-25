#!/usr/bin/env python3

from pprint import pprint

def fib_recursive(n, output_array):
    if n==1 or n==2:
        output_array.append(1)
        return 1
    else:
        fib = fib_recursive(n-1, output_array) + fib_recursive(n-2, output_array)
        output_array.append(fib)
        return fib


n = int(input("How long should your Fibonacci sequence be? Please input an integer.\n"))

output_array = []

fib_recursive(n, output_array)


pprint(output_array)
