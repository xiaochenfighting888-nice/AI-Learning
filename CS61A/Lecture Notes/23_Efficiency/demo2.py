def count_frames(f):
    """返回一个包装函数，记录当前活跃调用数和最大活跃调用数"""

    def counted(n):
        counted.open_count += 1

        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count

        result = f(n)

        counted.open_count -= 1
        return result

    # 表示当前尚未结束的函数调用数量
    counted.open_count = 0
    # 递归调用栈达到过的最大深度
    counted.max_count = 0
    return counted


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


if __name__ == "__main__":
    fib = count_frames(fib)
    print(fib(20))  # 6765
    print(fib.open_count)  # 0
    print(fib.max_count)  # 20
