
def fib(k):
    if k <= 0:
        return []
    elif k == 1:
        return [0]
    elif k == 2:
        return [0, 1]
    else:
        fib_sequence = fib(k - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

if __name__ == "__main__":
    k = int(input("Введіть кількість чисел Фібоначчі для виводу: "))
    fibonacci_numbers = fib(k)
    print(f"Перші {k} чисел Фібоначчі: {fibonacci_numbers}")
