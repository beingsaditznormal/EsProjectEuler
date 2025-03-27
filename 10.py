def sumPrimes(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False  # 0 e 1 non sono primi

    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False

    return sum(p for p, is_prime in enumerate(sieve) if is_prime)

result = sumPrimes(2000000)
print(f"La somma dei numeri primi inferiori a 2 milioni è {result}.")
