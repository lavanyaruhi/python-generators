#Squared numbers and skipping multiples of 3
def square_gen(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0:
            continue
        yield num ** 2
print("Squared numbers (skipping multiples of 3):")
s_num = int(input("enter the start of the integer:"))
e_num = int(input("enter the end of the integer:"))
sqrs = square_gen(s_num, e_num)
for sqr in sqrs:
    print(sqr)
