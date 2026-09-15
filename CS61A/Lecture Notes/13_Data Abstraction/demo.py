from math import gcd

# ---------- ADT 实现 ----------
# 构造函数和选择函数

# def rational(n, d):
#     # gcd计算整数 n 和 d 的最大公约数
#     g = gcd(n, d)
#     return [n // g, d // g]


# def numer(x):
#     """返回有理数 x 的分子"""
#     return x[0]


# def denom(x):
#     """返回有理数 x 的分母"""
#     return x[1]


def rational(n, d):
    def select(name):
        if name == "n":
            return n
        elif name == "d":
            return d

    return select


def numer(x):
    """返回有理数 x 的分子"""
    return x("n")


def denom(x):
    """返回有理数 x 的分母"""
    return x("d")


# ---------- 使用 ADT ----------


def add_rational(x, y):
    """返回两个有理数 x 和 y 的和"""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)

    return rational(nx * dy + ny * dx, dx * dy)


def mul_rational(x, y):
    """返回两个有理数 x 和 y 的积"""
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def equal_rational(x, y):
    """判断两个有理数是否表示相同的值"""
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rational(x):
    """打印有理数 x"""
    print(numer(x), "/", denom(x))


if __name__ == "__main__":
    x = rational(1, 2)
    y = rational(1, 3)

    print_rational(x)
    print_rational(y)
    print_rational(add_rational(x, y))
    print_rational(mul_rational(x, y))
    print(equal_rational(rational(1, 2), rational(2, 4)))
