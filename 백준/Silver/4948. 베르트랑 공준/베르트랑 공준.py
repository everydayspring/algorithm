import sys

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
                
    return is_prime

limit = 123456 * 2
is_prime = sieve_of_eratosthenes(limit)

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    print(sum(is_prime[n + 1: 2 * n + 1]))
