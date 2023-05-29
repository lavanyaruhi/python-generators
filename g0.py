def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
        #return i

# Create a generator object
generator = count_up_to(5)
print(generator)

# Iterate over the generator
for num in generator:
    print(num)
