def powers_of_two(exponent):
    power = 0
    while power <= exponent:
        yield 2 ** power
        power += 1
max_exponent = 7
power_generator = powers_of_two(max_exponent)

print(f"Powers of 2 up to exponent {max_exponent}:")
for power in power_generator:
    print(power)
