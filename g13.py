def prime_generator(numbers):
    for number in numbers:
        if is_prime(number):
            yield number

def is_prime(number):
    if number < 2:
        return False
    for i in range(2,number): # int(number ** 0.5) + 1
        if number % i == 0:
            return False
    return True
# my_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
# prime_generator = prime_generator(my_numbers)
# print("Prime numbers:")
s=int(input("enter start integer:"))
e=int(input("enter end integer:"))
numbers=range(s,e)
for prime in prime_generator(numbers):
    print(prime)
