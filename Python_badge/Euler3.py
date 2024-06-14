### Find The Largest Prime Factor of 600851475143

def largest_prime_factor(value):
    factor = 2
    while factor * factor <= value:
        if value % factor!=0:
            factor += 1
        else:
            value //= factor
    return value

print(largest_prime_factor(600851475143))
    