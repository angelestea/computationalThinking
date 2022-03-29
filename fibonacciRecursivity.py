def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Wirte a number:  "))
print(f'El ciclo de fibinacci se repetido {n} veces es {fibonacci(n)}')