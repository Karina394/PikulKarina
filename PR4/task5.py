name = "Karina"
surname = "Pikul"
group = "IT-32"

d = 24
c = 5

n = d * c

print(f"{name} {surname}, {group}")
print(f"n = {d} * {c} = {n}")

divisors = []
divisors_sum = 0

for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)
        divisors_sum += number

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")


is_prime = True

if n < 2:
    is_prime = False
else:
    for number in range(2, n):
        if n % number == 0:
            is_prime = False
            break
    else:
        is_prime = True

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")


primes = []

for number in range(2, n + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        primes.append(number)

print("Primes up to 120:", *primes)
print(f"Primes count: {len(primes)}")