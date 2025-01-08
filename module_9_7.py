def is_prime(func):
    def wrapper(*args):
        summ = func(*args)
        prime_number = True
        if summ < 2:
            return f'{summ} — Не является ни простым, ни составным числом'
        for i in range(2, summ):
            if summ % i == 0:
                prime_number = False
        if prime_number:
            return f'{summ} — Простое число'
        else:
            return f'{summ} — Составное число'
    return wrapper

@ is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(0, 0, 1)
print(result)
result = sum_three(1, 4, 1)
print(result)
result = sum_three(2, 3, 6)
print(result)