
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(a, b):
    primes = []
    for num in range(min(a, b), max(a, b) + 1):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    a = int(input("Введіть число a: "))
    b = int(input("Введіть число b: "))
    primes = find_primes(a, b)
    print(f"Прості числа між {a} та {b}: {primes}")
