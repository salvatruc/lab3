# Вводим верхнюю границу диапазона
N = int(input("Введите число N: "))

# Проверяем все числа от 2 до N
print("Простые числа от 1 до", N, ":")

for num in range(2, N + 1):
    is_prime = True

    # Проверяем делители числа
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Выводим число, если оно простое
    if is_prime:
        print(num)
