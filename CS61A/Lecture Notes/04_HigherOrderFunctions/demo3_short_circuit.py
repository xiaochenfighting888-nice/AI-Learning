from math import sqrt


def has_big_sqrt(x):
    """判断x的平方根是否大于10"""
    return x >= 0 and sqrt(x) > 10


print(has_big_sqrt(100))
# 这里不会报错，因为在判断x>=0为假了之后，就完成整个表达式的求值，不会继续判断后续表达式了，因此不会执行sqrt(-100)
print(has_big_sqrt(-100))


def reasonable(n):
    """or短路求值：当n==0为true时，不会计算1/n"""

    return n == 0 or 1 / n != 0


def main():
    print(has_big_sqrt(100))
    # 由于x >= 0为False，and后面的sqrt(x)不会执行
    print(has_big_sqrt(-100))

    print(reasonable(0))
    print(reasonable(10**10000))


if __name__ == "__main__":
    main()
