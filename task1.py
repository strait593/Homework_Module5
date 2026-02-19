def caching_fibonacci():
    cache = {}

    def fib_inner(n):
        if n <= 1:
            return 0
        
        if n == 1:
            return 1

        cache[n] = (n - 1) + (n - 2)
        return cache[n]

    return fib_inner

fib = caching_fibonacci()

print(fib(5))
print(fib(7))
print(fib(10))