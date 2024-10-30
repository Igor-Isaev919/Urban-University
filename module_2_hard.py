n = int(input("Привет, авантюрист! Пора испытать удачу: "))


def trap(n):
    result = ''
    if n < 3 or n > 20:
        exit(print("Ответ не верный. Game Over"))
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return f'{n} - {result}\n Поздравляю! You Win'


print(trap(n))
