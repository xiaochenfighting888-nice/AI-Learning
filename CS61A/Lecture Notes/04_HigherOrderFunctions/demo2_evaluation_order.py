from math import sqrt


def real_sqrt1(x):
    """返回x的平方根的实部"""
    if x >= 0:
        return sqrt(x)
    else:
        # 如果是负数，它的实部就是0
        return 0


def if_(c, t, f):
    """用函数模拟if表达式"""
    if c:
        return t
    else:
        return f


# 用函数调用实现
def real_sqrt2(x):
    """演示：函数调用会先对所有参数求值，因此这里不能正确处理负数"""
    return if_(x >= 0, sqrt(x), 0)


def main():
    print(real_sqrt1(16))
    print(real_sqrt1(-16))
    # 这会报错，因为求值过程中，先确定调用的函数以及执行主体之前求值它的参数
    # sqrt(-16)对负数进行平方根运算是错的
    # 调用表达式不允许跳过对调用表达式的参数部分进行求值过程，因此在执行函数主体之前，所有参数都会进行求值
    print(real_sqrt2(-16))


if __name__ == "__main__":
    main()
