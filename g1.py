def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

limit = 100
fibonacci_sequence = fibonacci_generator(limit)

# Iterate over the Fibonacci sequence and print each number
#for number in fibonacci_sequence:
 #   print(number)
print(fibonacci_sequence)
# Convert the Fibonacci sequence to a list
fibonacci_list = list(fibonacci_generator(limit))
print(fibonacci_list)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fibonacci = fibonacci_generator()
#for _ in range(10):
    #print(next(fibonacci))

