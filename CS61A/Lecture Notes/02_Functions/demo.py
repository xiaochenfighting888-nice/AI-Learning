# Functions demo
from math import pi
from operator import mul


def main():
    # 赋值语句
    radius = 10
    # 一条语句可以将多个名字绑定到值
    area, circ = pi * radius * radius, 2 * pi * radius
    print(area)
    print(circ)

    radius = 20
    # 赋值语句不同步：尽管radius改成20，但是area还是314.1592653589793
    print(area)

    # 赋值语句可以用来给函数起名字
    f = max
    print(f(2, -1))

    # 自定义函数
    def square(x):
        return mul(x, x)

    print(square(5))

    print(print(1), print(2))
    print(None)


if __name__ == "__main__":
    main()
