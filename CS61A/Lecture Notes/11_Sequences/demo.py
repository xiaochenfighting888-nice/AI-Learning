def divisors(n):
    """返回正整数 n 的所有正因数"""
    return [x for x in range(1, n + 1) if n % x == 0]


if __name__ == "__main__":
    print(divisors(9))  # [1, 3, 9]
