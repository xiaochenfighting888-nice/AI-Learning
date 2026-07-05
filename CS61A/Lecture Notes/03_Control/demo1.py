from operator import add, mul, truediv, floordiv, mod


def main():
    # 加法
    print(2 + 2)
    print(add(2, 2))
    # 乘法
    print(5 * 5)
    print(mul(5, 5))
    # 真除法：返回浮点数，保留小数部分
    print(2026 / 10)
    print(truediv(2026, 10))
    # 整除法：向下取整，结果类型取决于操作数
    print(2026 // 10)
    print(floordiv(2026, 10))
    # 取余
    print(2026 % 10)
    print(mod(2026, 10))

    # 返回n除以d的商和余数的函数
    def divide_exact(n, d):
        return n // d, n % d

    quotient, remainder = divide_exact(2026, 10)
    print(quotient)
    print(remainder)


if __name__ == "__main__":
    main()
