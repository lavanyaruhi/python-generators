def integer_partition_generator(n):
    if n == 0:
        yield []
        return

    for i in range(1, n + 1):
        for p in integer_partition_generator(n - i):
            yield [i] + p
num=int(input("enter integer number:"))
partions=integer_partition_generator(num)
print(f"All partitions of {num}:")
print(partions)
for partion in partions:
    print(partion)
   