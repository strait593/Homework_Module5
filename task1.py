def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(5))
print(fib(7))
print(fib(10))

# ФУНКЦІЯ caching_fibonacci
#     Створити порожній словник cache

#     ФУНКЦІЯ fibonacci(n)
#         Якщо n <= 0, повернути 0
#         Якщо n == 1, повернути 1
#         Якщо n у cache, повернути cache[n]

#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         Повернути cache[n]

#     Повернути функцію fibonacci
# КІНЕЦЬ ФУНКЦІЇ caching_fibonacci