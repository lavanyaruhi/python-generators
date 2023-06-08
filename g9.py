#Implement a generator function that yields prime factors of a given num.

def prime_factors(num):
    # Find prime factors
    factor = 2
    while factor * factor <= num:
        if num % factor == 0:
            yield factor
            num //= factor
        else:
            factor += 1
    if num > 1:
        yield num
l1=[3,5,7,9,11,15]
s=prime_factors(15)
for i in s:
    print(i)
