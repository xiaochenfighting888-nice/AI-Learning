# trace1 是一个“装饰器函数”
# fn 接收被装饰的函数
def trace1(fn):

    # traced 是包装后的新函数
    # x 是调用函数时传进来的参数
    def traced(x):

        # 在真正执行原函数 fn 之前，
        # 先打印：调用的是哪个函数、传入的参数是什么
        print("Calling", fn, "on argument", x)

        # 调用原来的函数 fn(x)
        # 并把原函数的返回值返回出去
        return fn(x)

    # 装饰器最终返回 traced 函数
    return traced


# @trace1
# def square(x):
#     return x * x
#
# 实际等价于：
#   def square(x):
#     return x * x
# square = trace1(square)
# square 这个名字指向的已经不是原来的 square，而是 trace1 返回的 traced 函数


@trace1  # @trace1 是装饰器语法
def square(x):
    # 返回 x 的平方
    return x * x


@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        # 计算 1² + 2² + ... + n²
        total, k = total + square(k), k + 1
    return total


if __name__ == "__main__":
    print(square(12))
    print(sum_squares_up_to(5))
