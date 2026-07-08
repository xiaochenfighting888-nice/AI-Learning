def fib(n):
    """返回斐波那契数列的第n项"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def main():
    print(fib(7))


if __name__ == "__main__":
    main()
