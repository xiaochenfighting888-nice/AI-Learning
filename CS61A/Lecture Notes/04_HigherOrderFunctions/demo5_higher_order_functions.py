def sum_naturals1(n):
    """
    求1~n的自然数之和

    >>> sum_naturals1(5)
    15
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


def sum_cubes1(n):
    """
    求1~n的立方和

    >>> sum_cubes1(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


# ______________________________________________________
"""
高阶函数的作用：
	1.表达通用的计算方法。summation不关心怎么计算每一项（是立方、平方还是开根号），它只关心“求和”这个通用逻辑。
	2.消除代码重复。只需要写一个summation，通过传入不同函数来复用逻辑
	3.在函数之间分离关注点。summation负责“循环和累加”，cube负责“计算立方”。它们各司其职，互不干扰
"""

"""泛化计算过程"""


def identity(k):
    return k


def cube(k):
    return pow(k, 3)


def pi_term(k):
    return 8 / ((4 * k - 3) * (4 * k - 1))


def summation(n, term):
    """计算term(1) + term(2) + ... + term(n)"""
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def sum_naturals2(n):
    """
    求1~n的自然数之和

    >>> sum_naturals2(5)
    15
    """
    return summation(n, identity)


def sum_cubes2(n):
    """
    求1~n的立方和

    >>> sum_cubes2(5)
    225
    """
    return summation(n, cube)


def sum_pi(n):
    """使用级数近似计算pi"""
    return summation(n, pi_term)


print(sum_pi(100000))
