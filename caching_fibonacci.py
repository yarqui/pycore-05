def caching_fibonacci():
    cache = {0: 0, 1: 1}

    def fibonacci(n: int) -> int:
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"Invalid input {n}. Must be a non-negative integer.")

        if n in cache:
            return cache[n]  # return cached value

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # memoize value

        return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(10))
print(fib(15))
