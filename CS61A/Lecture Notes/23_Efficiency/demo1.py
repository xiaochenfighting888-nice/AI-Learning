def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(f):
    """返回一个包装函数，用于统计函数被调用的次数"""

    def counted(n):
        counted.call_count += 1
        return f(n)

    counted.call_count = 0
    return counted


def memo(f):
    """返回一个带缓存的函数，避免对相同参数重复计算"""
    cache = {}

    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return memoized


if __name__ == "__main__":
    fib = count(fib)
    counted_fib = fib
    fib = memo(fib)
    fib = count(fib)
    print(fib(30))  # 832040
    print(fib.call_count)  # 59
    print(counted_fib.call_count)  # 31
