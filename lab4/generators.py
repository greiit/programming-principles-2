#1
N = int(input())
def square_generator(N):
    for i in range(1, N+1):
        yield i**2
squares_up_to_N = square_generator(N)
squares = list(squares_up_to_N)
print(squares)

#2
n = int(input())
def printing_it(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i
even_numbers_n = printing_it(n)
evens = list(even_numbers_n)
print(evens)

#3
n = int(input())
def printing_it(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
numbers_divisible = printing_it(n)
nums = list(numbers_divisible)
print(nums)

#4
a = int(input())
b = int(input())
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
for square in squares(a, b):
    print(square)

#5
n = int(input())
def decreasing_n(n):
    while n >= 0:
        yield n
        n -=1
for number in decreasing_n(n):
    print(number)