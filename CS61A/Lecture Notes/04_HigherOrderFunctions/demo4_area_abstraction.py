from math import pi, sqrt


def area_square1(r):
    """边长为r正方形的面积"""
    return r * r


def area_circle1(r):
    """半径为r的圆形面积"""
    return r * r * pi


def area_hexagon1(r):
    """边长为r的六边形面积"""
    return r * r * 3 * sqrt(3) / 2


# 边长是负数，也能输出结果是不对的
print(area_hexagon1(-10))

# ——————————————————————————————————————————————————————————
"""参数泛化模式"""


def area(r, shape_constant):
    # 断言语句，以assert开头，后面是一个布尔上下文表达式，后面再跟上打印信息。如果表达式的值为假，则会打印错误信息；如果表达式的值为真，没有输出。
    assert r > 0, "长度必须是正数"
    return r * r * shape_constant


def area_square2(r):
    """正方形的面积"""
    return area(r, 1)


def area_circle2(r):
    """圆形的面积"""
    return area(r, pi)


def area_hexagon2(r):
    """六边形的面积"""
    return area(r, 3 * sqrt(3) / 2)


print(area_square2(10))
