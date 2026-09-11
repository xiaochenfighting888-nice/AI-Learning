def search(f):
    """返回使 f(x) 为 True 的最小非负整数 x"""
    x = 0
    while not f(x):
        x += 1
    return x


def square(x):
    """返回 x 的平方"""
    return x * x


def inverse(f):
    """
    返回一个函数，该函数寻找满足 f(x) == y 的非负整数 x
    如果不存在这样的 x，搜索将不会终止
    """

    return lambda y: search(lambda x: f(x) == y)


if __name__ == "__main__":
    # 利用 inverse 构造整数范围内的“平方根函数”
    # 仅当 y 是完全平方数时才能找到结果，否则搜索不会终止
    sqrt = inverse(square)
    print(sqrt(100))  # 10
